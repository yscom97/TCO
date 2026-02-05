import math

class FleetSimulation:
    def __init__(self,
                 truck_count=9,
                 vehicle_price=3250000,  # Ex-showroom (INR)
                 body_building=250000,   # 특장 비용
                 registration_ins=180000,# 등록비 및 초기 보험료
                 down_payment_pct=0.10,  # 선수금 비율 (10%)
                 interest_rate=0.095,    # 연 이자율 (9.5%)
                 loan_tenure=48,         # 할부 개월 수
                 mileage=3.5,            # 연비 (km/L)
                 diesel_price=92.44,     # 디젤 가격 (INR/L)
                 adblue_pct=0.05,        # 디젤 대비 요소수 소모 비용 비율
                 driver_salary=22000,    # 운전기사 기본급
                 driver_bata=500,        # 운전기사 일비 (Bata)
                 maintenance_per_km=2.5, # km당 정비비 (타이어 포함)
                 toll_per_trip=300,      # 회당 통행료
                 bribe_per_trip=200,     # 회당 기타 비용 (비공식 비용 등)
                 trip_distance=120,      # 왕복 운행 거리 (km)
                 market_rate=16500       # 시장 운임 (Trip당 매출)
                 ):
        
        # 초기화
        self.truck_count = truck_count
        self.on_road_price = vehicle_price + body_building + registration_ins
        self.loan_amount = self.on_road_price * (1 - down_payment_pct)
        self.down_payment = self.on_road_price * down_payment_pct
        self.interest_rate = interest_rate
        self.loan_tenure = loan_tenure
        self.mileage = mileage
        self.diesel_price = diesel_price
        self.adblue_factor = 1 + adblue_pct
        self.driver_salary = driver_salary
        self.driver_bata = driver_bata
        self.maintenance_per_km = maintenance_per_km
        self.toll_per_trip = toll_per_trip
        self.bribe_per_trip = bribe_per_trip
        self.trip_distance = trip_distance
        self.market_rate = market_rate

    def calculate_emi(self):
        """월 할부금(EMI) 계산"""
        monthly_rate = self.interest_rate / 12
        emi = (self.loan_amount * monthly_rate * ((1 + monthly_rate) ** self.loan_tenure)) / \
              (((1 + monthly_rate) ** self.loan_tenure) - 1)
        return emi

    def run_monthly_analysis(self, trips_per_month):
        """월간 수익성 분석 실행"""
        # 1. 운행 지표
        total_distance = trips_per_month * self.trip_distance
        
        # 2. 고정비 (Fixed Costs)
        emi = self.calculate_emi()
        driver_total_cost = self.driver_salary + (self.driver_bata * trips_per_month) # 운행일수만큼 Bata 지급
        insurance_tax_monthly = 10000 # 월 할당 보험료 및 세금 (추정치)
        admin_cost = 3000 # 관리비
        
        total_fixed_cost = emi + driver_total_cost + insurance_tax_monthly + admin_cost

        # 3. 변동비 (Variable Costs)
        fuel_cost = (total_distance / self.mileage) * self.diesel_price * self.adblue_factor
        maintenance_cost = total_distance * self.maintenance_per_km
        toll_bribe_cost = trips_per_month * (self.toll_per_trip + self.bribe_per_trip)
        
        total_variable_cost = fuel_cost + maintenance_cost + toll_bribe_cost

        # 4. 총 비용 및 매출
        total_cost = total_fixed_cost + total_variable_cost
        revenue = trips_per_month * self.market_rate
        profit = revenue - total_cost
        profit_margin = (profit / revenue) * 100 if revenue > 0 else 0
        
        # 5. 손익분기점 (BEP) 계산 (고정비를 공헌이익(매출-변동비)으로 커버)
        variable_cost_per_trip = total_variable_cost / trips_per_month if trips_per_month > 0 else 0
        contribution_margin_per_trip = self.market_rate - variable_cost_per_trip
        bep_trips = math.ceil(total_fixed_cost / contribution_margin_per_trip) if contribution_margin_per_trip > 0 else 999

        return {
            "trips": trips_per_month,
            "revenue": revenue,
            "fixed_cost": total_fixed_cost,
            "variable_cost": total_variable_cost,
            "total_cost": total_cost,
            "profit": profit,
            "margin": profit_margin,
            "bep_trips": bep_trips
        }

    def print_report(self, trips_per_month=24):
        """상세 보고서 출력"""
        data = self.run_monthly_analysis(trips_per_month)
        
        fleet_revenue = data['revenue'] * self.truck_count
        fleet_profit = data['profit'] * self.truck_count
        fleet_capex = self.on_road_price * self.truck_count
        
        print("="*60)
        print(f"🚛 첸나이 운송 사업 타당성 시뮬레이션 보고서")
        print(f"차량: Ashok Leyland AVTR 2820 (9대) | 구간: 첸나이 항 ↔ Oragadam")
        print("="*60)
        
        print(f"\n[1] 대당 월간 운영 성과 (가동일수: {trips_per_month}일)")
        print(f" - 예상 매출액: ₹ {data['revenue']:,.0f}")
        print(f" - 총 운영비용: ₹ {data['total_cost']:,.0f}")
        print(f"    ├ 고정비 (EMI, 인건비 등): ₹ {data['fixed_cost']:,.0f}")
        print(f"    └ 변동비 (연료, 통행료 등): ₹ {data['variable_cost']:,.0f}")
        print(f" - 순이익 (Net Profit): ₹ {data['profit']:,.0f}")
        print(f" - 영업 이익률: {data['margin']:.1f}%")
        
        print(f"\n[2] 9대 전체 사업성 (Fleet Scale)")
        print(f" - 초기 투자비용 (CAPEX): ₹ {fleet_capex:,.0f} (약 {fleet_capex/10000000:.2f} Cr)")
        print(f" - 월간 총 순이익: ₹ {fleet_profit:,.0f}")
        print(f" - 연간 예상 순이익: ₹ {fleet_profit * 12:,.0f} (약 {(fleet_profit * 12)/100000:.1f} Lakhs)")
        
        print(f"\n[3] 손익분기 분석 (Risk Analysis)")
        print(f" - 손익분기 회전율(BEP): 월 {data['bep_trips']}회 왕복 시 본전")
        print(f" - 현재 가동률 대비 여유: {trips_per_month - data['bep_trips']}회 (안전 마진)")
        
        roi_months = (self.down_payment * self.truck_count) / fleet_profit if fleet_profit > 0 else 999
        print(f" - 자기자본(선수금) 회수 기간: 약 {roi_months:.1f}개월")
        print("="*60)

# --- 시뮬레이션 실행 ---

# 시나리오 1: 기본 가정 (월 24회 운행)
sim = FleetSimulation()
print("\n>>> 시나리오 1: 정상 운영 (월 24회 회전)")
sim.print_report(trips_per_month=24)

# 시나리오 2: 항만 혼잡으로 회전율 하락 (월 18회 운행)
print("\n\n>>> 시나리오 2: 항만 혼잡 발생 (월 18회 회전 - Risk Case)")
sim.print_report(trips_per_month=18)

# 시나리오 3: 더블 드라이버 투입으로 회전율 극대화 (월 30회 운행, 인건비 상승 반영)
# 인건비 상승(기사 1명 추가: +25,000 INR) 반영하여 시뮬레이터 재설정
print("\n\n>>> 시나리오 3: 2인 승무 풀가동 (월 30회 회전 - Max Revenue)")
sim_high_perf = FleetSimulation(driver_salary=45000) # 기사 2명분 급여 대략 반영
sim_high_perf.print_report(trips_per_month=30)
```