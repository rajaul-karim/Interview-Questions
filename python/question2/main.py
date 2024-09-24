"""
Question 2: Auto Scaling Decision Script

Problem:
Write a script that simulates a simple auto-scaling decision mechanism for a cloud service. The script will receive CPU utilisation as input of a list of instance and decide whether to scale up or scale down the number of servers.

1. If the average CPU utilisation is greater than 75% over the last 10 data points, scale up by increasing the number of servers by 1.
2. If the average CPU utilisation is below 25% over the last 10 data points, scale down by reducing the number of servers by 1.
3. Otherwise, maintain the current number of servers.

Requirements:
1. Input: List of CPU utilisation percentages for the last 10 data points.
2. Output: A decision (scale up, scale down, or maintain current).
"""
import json

CPU_UTILISATION_FILE_PATH = "cpu_utilisation.json"


def _get_cpu_utilization(file_path: str) -> list[dict[str, str | int]]:
    """
    Read the CPU data from a json file and return a list of dictionaries containing the CPU data.

    :param file_path: The path to the file containing the CPU data.
    :return: A list of dictionaries containing the CPU data.
    """
    with open(file_path, 'r') as file:
        cpu_data = json.load(file)
    return cpu_data


def auto_scaling_decision(cpu_data: list[int], current_servers: int) -> tuple[str, int]:
    """
    @DocString
    """
    pass


if __name__ == "__main__":
    pass
