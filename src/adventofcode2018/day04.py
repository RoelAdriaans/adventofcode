import re
from collections import Counter

from adventofcode.utils.abstract import FileReaderSolution


class Day4:
    @staticmethod
    def split_line_into_sections(input_data: str) -> dict:
        """Split the input into sections we can use:
            [1518-11-01 00:00] Guard #10 begins shift
        year-month-day hour:minute
        """
        date_pattern = (
            r"^\[\d*-(?P<month>\d*)-(?P<day>\d*) (?P<hour>\d*):(?P<minute>\d*)]"
        )
        guard_pattern = r"Guard #(?P<guard>\d*) begins shift"

        time_result = re.match(date_pattern, input_data)
        guard_result = re.search(guard_pattern, input_data)

        if guard_result:
            guard = int(guard_result["guard"])
            mode = "guard"
        else:
            guard = False
            if "asleep" in input_data:
                mode = "asleep"
            elif "wakes" in input_data:
                mode = "wakes"
            else:
                raise ValueError(f"Error during in {input_data}, no valid state")

        result = {
            "month": int(time_result["month"]),
            "day": int(time_result["day"]),
            "hour": int(time_result["hour"]),
            "minute": int(time_result["minute"]),
            "mode": mode,
            "guard": guard,
        }

        return result

    def parse_strings(self, input_data):
        """
        Split the input data into objects we can use. Objects are sorted on
        date/time.
        """
        lines = input_data.split("\n")
        log_entries = [self.split_line_into_sections(line) for line in lines if line]
        sorted_log_entries = sorted(
            log_entries, key=lambda x: (x["month"], x["day"], x["hour"], x["minute"])
        )
        return sorted_log_entries

    def parse_logs(self, log_entries):
        guard_info = {}
        current_guard = 0
        sleep = 0
        for entry in log_entries:
            if entry["mode"] == "guard":
                # We have a new guard. Set ID and append entry into info dict
                current_guard = entry["guard"]
                if current_guard not in guard_info:
                    guard_info[current_guard] = []
            elif entry["mode"] == "asleep":
                sleep = entry["minute"]
            else:
                sleep_time = list(range(sleep, entry["minute"] + 1))
                guard_info[current_guard].append(sleep_time)
        return guard_info

    @staticmethod
    def determine_most_asleep_minute(guard_info: list) -> int:
        """Determine which minute this guard sleeps the most"""
        minutes_slept = Counter()
        for shift in guard_info:
            for minute in shift:
                minutes_slept[minute] += 1
        if minutes_slept.most_common(1):
            return minutes_slept.most_common(1)[0][0]
        else:
            return False


class Day4PartA(Day4, FileReaderSolution):
    @staticmethod
    def determine_mostasleep(guard_info):
        most_slept_guard = False
        total_minutes_slept = False
        for guard_id, minutes_slept in guard_info.items():
            # Get the minutes a guard slept. Subtract one, since we add all the minutes
            # but the minut the guard falls asleep doesn't found.
            this_guard_slept = sum([len(x) - 1 for x in minutes_slept])
            if this_guard_slept > total_minutes_slept:
                total_minutes_slept = this_guard_slept
                most_slept_guard = guard_id
        return most_slept_guard, total_minutes_slept

    def solve(self, input_data: str) -> int:
        log_entries = self.parse_strings(input_data)
        guard_info = self.parse_logs(log_entries)
        guard_id, minutes_slept = self.determine_mostasleep(guard_info)
        most_slept_minute = self.determine_most_asleep_minute(guard_info[guard_id])
        result = guard_id * most_slept_minute
        return result


class Day4PartB(Day4, FileReaderSolution):
    @staticmethod
    def determine_most_asleep_same_minute(guard_info: dict) -> (int, int):
        """
        Determine which guard is the most asleep at the same minute
        """
        guard_most_slept_same_minute = False
        times_that_guard_slept = False
        minute_that_guard_slept = False
        for guard_id, minutes_slept in guard_info.items():
            minute = Day4.determine_most_asleep_minute(minutes_slept)
            # Count how many minutes this guard slept at the specific minute
            total_minutes_slept = 0
            for day in minutes_slept:
                if minute in day:
                    total_minutes_slept += 1
            if total_minutes_slept > times_that_guard_slept:
                guard_most_slept_same_minute = guard_id
                times_that_guard_slept = total_minutes_slept
                minute_that_guard_slept = minute

        return guard_most_slept_same_minute, minute_that_guard_slept

    def solve(self, input_data: str) -> int:
        log_entries = self.parse_strings(input_data)
        guard_info = self.parse_logs(log_entries)
        guard, minute = self.determine_most_asleep_same_minute(guard_info)
        result = guard * minute
        return result
