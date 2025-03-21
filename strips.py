{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPbZplEyGUZTGI59GhgjH4r",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/faizulhz/ProgrammingAssignment2/blob/master/strips.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "sbtr7vrRPyAe"
      },
      "outputs": [],
      "source": [
        "class Action:\n",
        "    def __init__(self, name, preconditions, add_effects, del_effects):\n",
        "        self.name = name\n",
        "        self.preconditions = set(preconditions)\n",
        "        self.add_effects = set(add_effects)\n",
        "        self.del_effects = set(del_effects)\n",
        "\n",
        "    def is_applicable(self, state):\n",
        "        return self.preconditions.issubset(state)\n",
        "\n",
        "    def apply(self, state):\n",
        "        new_state = state - self.del_effects\n",
        "        new_state |= self.add_effects\n",
        "        return new_state\n",
        "\n",
        "    def __str__(self):\n",
        "        return self.name\n",
        "\n",
        "def strips_planner(initial_state, goal_state, actions):\n",
        "    from collections import deque\n",
        "\n",
        "    frontier = deque()\n",
        "    frontier.append((initial_state, []))\n",
        "    visited = set()\n",
        "\n",
        "    while frontier:\n",
        "        current_state, plan = frontier.popleft()\n",
        "\n",
        "        if goal_state.issubset(current_state):\n",
        "            return plan\n",
        "\n",
        "        state_key = frozenset(current_state)\n",
        "        if state_key in visited:\n",
        "            continue\n",
        "        visited.add(state_key)\n",
        "\n",
        "        for action in actions:\n",
        "            if action.is_applicable(current_state):\n",
        "                next_state = action.apply(current_state)\n",
        "                frontier.append((next_state, plan + [action]))\n",
        "\n",
        "    return None\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Define actions\n",
        "actions = [\n",
        "    Action(\"PickUp A\", [\"Clear A\", \"OnTable A\", \"HandEmpty\"], [\"Holding A\"], [\"Clear A\", \"OnTable A\", \"HandEmpty\"]),\n",
        "    Action(\"PutDown A\", [\"Holding A\"], [\"OnTable A\", \"Clear A\", \"HandEmpty\"], [\"Holding A\"]),\n",
        "    Action(\"Stack A on B\", [\"Holding A\", \"Clear B\"], [\"On A B\", \"Clear A\", \"HandEmpty\"], [\"Holding A\", \"Clear B\"]),\n",
        "    Action(\"Unstack A from B\", [\"On A B\", \"Clear A\", \"HandEmpty\"], [\"Holding A\", \"Clear B\"], [\"On A B\", \"Clear A\", \"HandEmpty\"]),\n",
        "]\n",
        "\n",
        "# Initial and goal states\n",
        "initial_state = set([\"OnTable A\", \"Clear A\", \"Clear B\", \"OnTable B\", \"HandEmpty\"])\n",
        "goal_state = set([\"On A B\"])\n",
        "\n",
        "# Run planner\n",
        "plan = strips_planner(initial_state, goal_state, actions)\n",
        "\n",
        "if plan:\n",
        "    print(\"Plan found:\")\n",
        "    for step in plan:\n",
        "        print(\" -\", step)\n",
        "else:\n",
        "    print(\"No plan found.\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tBlqVT4oQAgP",
        "outputId": "141aec6f-1248-43de-886d-e8e087e23096"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Plan found:\n",
            " - PickUp A\n",
            " - Stack A on B\n"
          ]
        }
      ]
    }
  ]
}