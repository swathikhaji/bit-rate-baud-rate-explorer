# Bit Rate and Baud Rate Explorer

## Project Overview

The **Bit Rate and Baud Rate Explorer** is a web-based Computer Networks mini project developed using Python and Streamlit. It helps users understand the relationship between bit rate, baud rate, and the number of bits represented by each symbol in a digital communication system.

The website provides an interactive calculator where users can enter a baud rate, select the number of bits per symbol, and calculate the theoretical bit rate.

## Objectives

- To understand the concepts of bit rate and baud rate.
- To calculate the theoretical bit rate of a digital communication system.
- To explore how the number of bits per symbol affects the bit rate.
- To provide a simple and interactive web interface for performing calculations.

## Technologies Used

- **Python** — Programming language
- **Streamlit** — Web application framework
- **GitHub** — Source code hosting and version control
- **Streamlit Community Cloud** — Website deployment and hosting

## Formula Used

The theoretical bit rate is calculated using the following formula:

**Bit Rate = Baud Rate × Bits per Symbol**

Where:

- **Bit Rate:** Number of bits transmitted per second, measured in bits per second (bps).
- **Baud Rate:** Number of symbols transmitted per second, measured in baud.
- **Bits per Symbol:** Number of bits represented by each symbol.

### Example Calculation

Given:

- Baud Rate = 1000 baud
- Bits per Symbol = 2

Calculation:

Bit Rate = 1000 × 2

**Result = 2000 bps (2 kbps)**

## Features

- Interactive bit rate calculator.
- User input for baud rate.
- Selection of bits per symbol.
- Automatic calculation of theoretical bit rate.
- Display of the calculation formula and result.
- Conversion of bit rate into kilobits per second (kbps).
- Simple and user-friendly web interface.

## How to Run the Project Locally

### Prerequisites

- Python installed on your computer.
- A code editor such as Visual Studio Code.

### Installation Steps

1. Clone or download this repository.
2. Open the project folder in Visual Studio Code.
3. Open the terminal in the project folder.
4. Install the required dependency:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:

   ```bash
   python -m streamlit run app.py
   ```

6. Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## Live Website

Access the deployed application here:

[Bit Rate and Baud Rate Explorer](https://bit-rate-baud-rate-explorer-kyagt3d9aseex7jul856p6.streamlit.app)

## Project Type

Computer Networks Mini Project — Python-based web application and simulation-free bit rate calculation interface.

## Conclusion

The Bit Rate and Baud Rate Explorer demonstrates how baud rate and bits per symbol determine the theoretical bit rate of a digital communication system. The interactive website makes these calculations easy to perform and helps students understand an important concept in Computer Networks.

This project is intended for educational purposes. The calculated bit rate is theoretical and does not represent actual network throughput.
