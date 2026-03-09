# Drillhole Monitoring Report Generator

This project generates **PDF reports with graphs** for drillhole monitoring data.
The report includes:

* Pressure measurements per channel
* Temperature measurements per channel
* Atmospheric pressure graphs
* Atmospheric pressure at sea level

The data is retrieved from a database, visualized using **Matplotlib**, and exported into a **PDF report using ReportLab**.

---

# Requirements

* Python 3.10+
* Access to the monitoring database

Required Python libraries:

* matplotlib
* reportlab

---

# Installation

Clone the repository:

```bash
git clone <https://github.com/Nurasick/Piezometrics.git>
cd <repository-folder>
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Project Structure

```
project/
│
├── export_pdf.py        # CLI entry point for generating reports
├── queries.py           # Database queries
├── plots.py             # Matplotlib plotting functions
├── pdf_builder.py       # PDF generation logic
├── config.py            # Configuration / environment variables
├── db.py                # DB connection
└── README.md
```

---

# Usage

The report is generated using a CLI command.

Example:

```bash
py export_pdf.py --drillholes 159421 159412 --from "2026-02-06T00:00:00" --to "2026-03-06T00:00:00" --output report.pdf
```

### Parameters

| Argument         | Description                  |
| --------------   | ---------------------------- |
| `--drillholes`   | List of drillhole IDs        |
| `--from`         | Start timestamp (ISO format) |
| `--to`           | End timestamp (ISO format)   |
| `--pressure_type`| choice of kPa, mbar, mH2)    |
| `--output`       | Output PDF file name         |

---

# Example

```bash
py export_pdf.py \
  --drillholes 159421 159412 \
  --from "2026-02-06T00:00:00" \
  --to "2026-03-06T00:00:00" \
  --pressure_type "kPa" \
  --output report.pdf
```

This command will:

1. Fetch measurements for the specified drillholes
2. Generate plots for:

   * pressure (per channel)
   * temperature (per channel)
   * atmospheric pressure
   * atmospheric pressure at sea level
3. Build a formatted PDF report

---

# Output

The generated PDF will contain:

* A **title page**
* Sections for each **drillhole**
* Separate graphs for:

  * Pressure per channel
  * Temperature per channel
  * Atmospheric pressure
  * Atmospheric pressure at sea level

---

# Notes

* Time parameters must be provided in YYYY-MM-DDTHH:MM:SS format.
* If no data is available for a graph, the report will show a **"No Data Available"** message.

---
