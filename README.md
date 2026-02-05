# Chennai Fleet TCO & Feasibility Simulator

CJ Logistics India Branch – Fleet TCO (Total Cost of Ownership) and feasibility simulator for Chennai operations.

## Features

- **CAPEX & Financing**: Vehicle cost, down payment, interest rate, tenure, fleet size
- **Operating (Fixed)**: Driver salary, bhatta, trip incentive, helper, insurance, road tax, admin
- **Operating (Variable)**: Diesel, mileage, tires, maintenance, AdBlue, FASTag
- **Market Benchmark**: Trip / Km / Ton unit types, market rate, trip distance, monthly trips
- **Results**: Monthly savings, break-even distance, cost per km/trip, sensitivity chart, cost breakdown
- **Report Export**: Save simulation as HTML report
- **AI Consultant**: Rule-based feasibility and risk analysis

## Run locally

Open `index.html` or `chennai_tco_simulator.html` in a browser (no server required; uses CDN for React, Tailwind, Recharts).

## Deploy on GitHub Pages

1. **Create a GitHub repository** (e.g. `TCO_Simulator`).

2. **Push this project** to the repo:
   ```bash
   git init
   git add index.html chennai_tco_simulator.html .nojekyll README.md
   git commit -m "Add TCO Simulator for GitHub Pages"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/TCO_Simulator.git
   git push -u origin main
   ```

3. **Enable GitHub Pages**:
   - Repo → **Settings** → **Pages**
   - **Source**: Deploy from a branch
   - **Branch**: `main` (or `master`)
   - **Folder**: `/ (root)`
   - Save

4. After a minute or two, the app will be available at:
   - **https://YOUR_USERNAME.github.io/TCO_Simulator/**

The `.nojekyll` file tells GitHub not to use Jekyll so that your HTML and assets are served as-is.

## License

Internal use – CJ Logistics.
