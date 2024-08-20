import numpy
from matplotlib import pyplot as plt


def data_to_dict(data):
    data_dict = {}
    for i in range(1, len(data)):
        row = data[i]
        name = row[0]
        steps = numpy.array(row[1:], dtype=int)
        data_dict[name] = steps
    return data_dict


def hourly_to_daily(hourly_steps):
    daily_steps = []

    for i in range(0, len(hourly_steps), 24):
        day_steps = hourly_steps[i:i + 24]
        daily_step_count = sum(day_steps)
        daily_steps.append(daily_step_count)
    return daily_steps


def compute_stats(step_dict):
    stats_dict = {}
    # Write your code here to iterates over the keys and values of step_dict and populates stats_dict with the same
    # keys, but their values as dictionaries containing "min", "max", and "average" numbers stored in them.
    for key, value in step_dict.items():
        stats_dict[key] = {"min": min(value), "max": max(value), "average": numpy.mean(value)}
    return stats_dict


def choose_categories(avg_list):
    categories = {"concerning": 0, "average": 0, "excellent": 0}
    for avg_steps in avg_list:
        if avg_steps < 5000:
            categories["concerning"] = categories["concerning"] + 1
        elif 5000 < avg_steps < 10000:
            categories["average"] = categories["average"] + 1
        else:
            categories["excellent"] = categories["excellent"] + 1
    return categories


def daily_to_total(daily_steps):
    total_dict = {}
    for name, steps in daily_steps.items():
        total_dict[name] = sum(steps)
    return total_dict


def find_min_index(input_list):
    current_min = input_list[0]
    index = 0
    for i in range(len(input_list)):
        if input_list[i] < current_min:
            current_min = input_list[i]
            index = i

    return index


def my_sort(user_names, user_steps):
    sorted_user_names = []
    sorted_user_steps = []
    for i in range(len(user_steps)):
        min_index = find_min_index(user_steps)
        sorted_user_names.append(user_names[min_index])
        sorted_user_steps.append(user_steps[min_index])
        user_steps[min_index] = float("inf")
    return sorted_user_names, sorted_user_steps


def plot_line(steps):
    # Make a list of hours in a day
    hour_list = range(24)
    # Making the line plot and defining the required labels
    plt.plot(hour_list, steps)
    plt.title("Performance over the day")
    plt.xlabel("Hour of the day")
    plt.ylabel("Number of steps")

    plt.show()


def plot_pie(categories):
    labels = categories.items()
    sizes = categories.values()

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels)
    plt.title("Pie chart for categories")
    plt.show()


def plot_bar(sorted_names, sorted_steps):
    fig, ax = plt.subplots()
    ax.bar(sorted_names, sorted_steps)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_bubbles(daily_step_dict):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    # Code to plot data for all users in a bubble plot.
    for name in daily_step_dict:
        plt.scatter(days, [name]*7, numpy.array(daily_step_dict[name])/30)
    plt.title("Bubble plot for all members")
    plt.xlabel("Day of the week")
    plt.ylabel("User name")
    plt.show()


def main():
    data = numpy.loadtxt("steps.csv", delimiter=",", dtype=str)
    data_dict = data_to_dict(data)

    daily_step_dict = {}
    # Write your code here that builds daily_step_dict in a loop using keys from data_dict and calling
    # hourly_to_daily function on its values
    for key in data_dict:
        daily_step_dict[key] = hourly_to_daily(data_dict[key])

    stats_dict = compute_stats(daily_step_dict)

    # separating out a list of averages
    avg_list = []
    for name in stats_dict:
        stats = stats_dict[name]
        avg_list.append(stats["average"])

    categories = choose_categories(avg_list)

    total_step_dict = daily_to_total(daily_step_dict)

    # relevant list formation and function calls
    unsorted_names = list(total_step_dict.keys())
    unsorted_steps = list(total_step_dict.values())
    sorted_names, sorted_steps = my_sort(unsorted_names, unsorted_steps)

    # list preparation and function call for line plot
    steps = data_dict["Juliana"][0:24]
    plot_line(steps)

    plot_pie(categories)

    plot_bar(sorted_names, sorted_steps)

    plot_bubbles(daily_step_dict)


main()
