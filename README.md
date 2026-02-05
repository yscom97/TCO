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

## Deploy on GitHub Pages (using your GitHub)

1. **Create the repo on GitHub** (if not exists):
   - Go to [github.com/new](https://github.com/new)
   - Repository name: `TCO_Simulator`
   - Public, no README/license (this project already has them)
   - Create repository

2. **Push from this project** (remote is set to `https://github.com/yskim/TCO_Simulator.git`):
   ```powershell
   cd "d:\03. Projects\TCO_Simulator"
   # One-time: set your Git identity (use your GitHub name/email)
   git config --global user.name "Your Name"
   git config --global user.email "your-email@example.com"
   # Push (browser or credential window will open for login)
   git push -u origin main
   ```
   Or run the script: `.\deploy.ps1`  
   If your GitHub username is not **yskim**, change the remote first:
   ```bash
   git remote set-url origin https://github.com/YOUR_USERNAME/TCO_Simulator.git
   ```

3. **Enable GitHub Pages**:
   - Repo → **Settings** → **Pages**
   - **Source**: Deploy from a branch
   - **Branch**: `main` (or `master`)
   - **Folder**: `/ (root)`
   - Save

4. After a minute or two, the app will be available at:
   - **https://yskim.github.io/TCO_Simulator/** (replace **yskim** with your GitHub username if different)

The `.nojekyll` file tells GitHub not to use Jekyll so that your HTML and assets are served as-is.

## License

Internal use – CJ Logistics.
