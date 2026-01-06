# shift_roaster.py
# Generates an Excel shift roster and a Leave Planner for a 10-person team.
# Usage: python shift_roaster.py
# Requires: pandas, openpyxl
# If missing: pip install pandas openpyxl

from datetime import datetime, timedelta
import pandas as pd
import os

TEAM = ["ashwini", "Balaji", "tarun", "vishnu", "Dhanu", "Dhana", "Santhosh", "Rathish", "Shamili", "prasad"]
ROTATION_STEP = 3  # at least 3 people rotated each week
WEEKS = 4          # default number of weeks to generate
OUT_XLSX = "shift_roster.xlsx"


def monday_of(date):
    return date - timedelta(days=date.weekday())


def rotate(lst, k):
    k = k % len(lst)
    return lst[k:] + lst[:k]


def build_roster(start_date, weeks=WEEKS):
    start_monday = monday_of(start_date)
    alpha_team = sorted(TEAM, key=lambda s: s.lower())
    roster_map = {}  # date -> {'morning': [...], 'afternoon': [...], 'note': ''}
    compoff_entries = []  # rows for leave planner (Date, Name, Type, Status, Notes)

    for w in range(weeks):
        week_monday = start_monday + timedelta(weeks=w)
        # rotate team for this week by ROTATION_STEP * w (cumulative)
        rotated = rotate(TEAM, (ROTATION_STEP * w))
        # weekday assignments (same for Mon-Fri)
        morning_group = rotated[:5]
        afternoon_group = rotated[5:]
        # fill Mon-Fri
        for d in range(5):
            day = week_monday + timedelta(days=d)
            roster_map[day.date()] = {
                "morning": list(morning_group),
                "afternoon": list(afternoon_group),
                "note": ""
            }
        # weekend: Saturday & Sunday -> single person (both days) chosen by alphabetical order cycling
        weekend_person = alpha_team[(w) % len(alpha_team)]
        for d in (5, 6):  # Sat, Sun
            day = week_monday + timedelta(days=d)
            roster_map[day.date()] = {
                "morning": [weekend_person],  # put weekend person in morning column (single)
                "afternoon": [],
                "note": "Weekend"
            }
        # add comp.off entries for the Monday & Tuesday after this weekend
        next_monday = week_monday + timedelta(weeks=1)
        for dd in (0, 1):  # Monday, Tuesday after weekend
            co_day = (next_monday + timedelta(days=dd)).date()
            compoff_entries.append({
                "Date": co_day,
                "Name": weekend_person,
                "Type": "CompOff",
                "Status": "Approved",
                "Notes": "Weekend comp.off"
            })

    return roster_map, compoff_entries


def apply_leave_planner_to_roster(roster_map, leave_df):
    # leave_df columns expected: Date, Name, Type, Status
    for _, row in leave_df.iterrows():
        try:
            date = pd.to_datetime(row["Date"]).date()
        except Exception:
            continue
        name = str(row["Name"]).strip()
        ltype = str(row.get("Type", "")).strip().lower()
        status = str(row.get("Status", "")).strip()
        suffix = ""
        if ltype == "compoff":
            suffix = "-compoff"
        elif ltype == "pto":
            suffix = f"-PTO-{status}" if status else "-PTO"
        else:
            # unknown types still get noted
            suffix = f"-{row.get('Type','Leave')}-{status}"

        if date in roster_map:
            # replace occurrences of name in morning/afternoon lists with annotated version
            for shift in ("morning", "afternoon"):
                newlist = []
                replaced = False
                for p in roster_map[date][shift]:
                    if p == name:
                        newlist.append(f"{p}{suffix}")
                        replaced = True
                    else:
                        newlist.append(p)
                # if leave applies but name not scheduled, still add note to 'note'
                if not replaced and name in [r["Name"] for _, r in []]:
                    pass
                roster_map[date][shift] = newlist
            # add note if not present
            if roster_map[date].get("note"):
                roster_map[date]["note"] += f"; {name}{suffix}"
            else:
                roster_map[date]["note"] = f"{name}{suffix}"


def roster_map_to_dataframe(roster_map):
    rows = []
    for date in sorted(roster_map.keys()):
        r = roster_map[date]
        dayname = date.strftime("%A")
        morning = ", ".join(r["morning"]) if r["morning"] else ""
        afternoon = ", ".join(r["afternoon"]) if r["afternoon"] else ""
        rows.append({
            "Date": date,
            "Day": dayname,
            "Morning": morning,
            "Afternoon": afternoon,
            "Note": r.get("note", "")
        })
    df = pd.DataFrame(rows)
    return df


def create_excel(start_date=None, weeks=WEEKS, out_file=OUT_XLSX):
    if start_date is None:
        start_date = datetime.today()
    roster_map, compoff_entries = build_roster(start_date, weeks=weeks)

    # Prepare Leave Planner with compoff prefilled
    leave_planner_df = pd.DataFrame(compoff_entries, columns=["Date", "Name", "Type", "Status", "Notes"])
    # Add an example PTO row template (user can edit/append in the Excel)
    template_row = {
        "Date": "",
        "Name": "",
        "Type": "PTO",
        "Status": "Pending",
        "Notes": "Fill Date, Name, change Status to Approved when okay"
    }
    leave_planner_df = pd.concat([leave_planner_df, pd.DataFrame([template_row])], ignore_index=True)

    # Apply leave planner annotations to roster (so comp.off appears in roster)
    apply_leave_planner_to_roster(roster_map, leave_planner_df)

    roster_df = roster_map_to_dataframe(roster_map)

    # Save Excel with two sheets: Roster and Leave Planner
    with pd.ExcelWriter(out_file, engine="openpyxl") as writer:
        roster_df.to_excel(writer, sheet_name="Roster", index=False)
        leave_planner_df.to_excel(writer, sheet_name="Leave Planner", index=False)
        # Add a short README sheet
        readme = pd.DataFrame([{
            "Info": "Edit 'Leave Planner' to add PTO rows. Set Type to PTO and Status to Pending/Approved. Re-run this script to update the Roster sheet to reflect PTO annotations (e.g., 'Rathish-PTO-pending' / 'Rathish-PTO-Approved'). Weekend assignee comp.off for next Mon/Tue are prefilled."
        }])
        readme.to_excel(writer, sheet_name="README", index=False)

    print(f"Roster written to {os.path.abspath(out_file)}")
    print("Open the file, edit 'Leave Planner' to add PTOs, then re-run the script to refresh the Roster.")


if __name__ == "__main__":
    # Example: generate for 4 weeks starting today
    create_excel(start_date=datetime.today(), weeks=WEEKS, out_file=OUT_XLSX)