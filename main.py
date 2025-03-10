{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPO5jCpOsndpxTONTOWh/B0",
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
        "<a href=\"https://colab.research.google.com/github/Yuan-Hessed-Vasig/CPE-103-00P-1-A/blob/main/main.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "n_w1GBx5wQSh"
      },
      "outputs": [],
      "source": [
        "\"\"\"\n",
        "    main.py\n",
        "\"\"\"\n",
        "import Accounts\n",
        "import ATM\n",
        "\n",
        "Account1 = Accounts.Accounts(account_number=191105,account_firstname=\"Justin Rhey\",\n",
        "                             account_lastname=\"Monoy\", current_balance = 1500,\n",
        "                             address = \"Caloocan City\",\n",
        "                             email =\"rheymonoy@gmail.com\")\n",
        "\n",
        "print(\"Account1\")\n",
        "print(Account1.account_firstname)\n",
        "print(Account1.account_lastname)\n",
        "print(Account1.current_balance)\n",
        "print(Account1.address)\n",
        "print(Account1.email)\n",
        "\n",
        "ATM1 = ATM.ATM(serial_number=1)\n",
        "ATM1.withdraw(Account1, 750)\n",
        "ATM1.check_current_balance(Account1)\n",
        "\n",
        "print(f\"\\nATM Serial Number: {ATM1.serial_number}\")\n",
        "\n",
        "Account2 = Accounts.Accounts(account_number=132497, account_firstname=\"Mina\",\n",
        "                             account_lastname=\"Myoui\", current_balance=5000,\n",
        "                             address=\"Seoul, South Korea\",\n",
        "                             email=\"minaimnida37@gmail.com\")\n",
        "\n",
        "print(\"\\nAccount2\")\n",
        "print(Account2.account_firstname)\n",
        "print(Account2.account_lastname)\n",
        "print(Account2.current_balance)\n",
        "print(Account2.address)\n",
        "print(Account2.email)\n",
        "\n",
        "ATM2 = ATM.ATM(serial_number=2)\n",
        "ATM2.deposit(Account2, 2345)\n",
        "ATM2.check_current_balance(Account2)\n",
        "\n",
        "print(f\"\\nATM Serial Number: {ATM2.serial_number}\")\n",
        "\n",
        "ATM1.view_transaction_summary()"
      ]
    }
  ]
}