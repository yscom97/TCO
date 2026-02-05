[PRD] 인도 첸나이 운송 자차 투입 TCO 시뮬레이터 요구사항 정의서

1. 프로젝트 개요 (Project Overview)

프로젝트명: Chennai Fleet TCO & Feasibility Simulator

작성자: IT Manager (CJ Logistics China)

배경: 인도 첸나이 지역의 물동량 증가에 따라, 기존 외주 운송(Market Hired) 방식을 자차 운영(Own Fleet)으로 전환할지 여부를 판단하기 위한 정량적 데이터 분석 도구 필요.

목표: 1. 첸나이 현지 비용 구조를 반영한 정밀 TCO(Total Cost of Ownership) 산출.
2. 다양한 시장 변수(유가, 운임, 가동률)에 따른 민감도 분석.
3. AI 기반의 자동화된 결과 분석 및 의사결정 제안 리포트 제공.

대상 차량: Ashok Leyland 20FT Triple Axle (총 9대)

2. 사용자 정의 (Target Audience)

Primary User: 물류 운영 매니저, 운송 담당자 (인도 법인)

Secondary User: 법인장, 재무 담당자 (투자 의사결정권자)

3. 기능적 요구사항 (Functional Requirements)

3.1. 입력 변수 관리 (Parameter Management)

사용자가 직접 수정 가능해야 하며, 인도 현지 운송 시장의 특수성을 반영해야 한다.

A. 차량 및 금융 (CAPEX)

차량: 차량 단가 (Chassis + Body Building 비용 포함)

금융: 선수금 비율(%), 이자율(%), 할부 기간(개월), 잔존 가치(Residual Value)

B. 운영 비용 (OPEX - Fixed)

인건비 (복합 구조):

기사 기본급 (Monthly Fixed Salary)

일일 수당 (Daily Bhatta) - 운행 일수에 연동

트립 인센티브 (Per Trip Incentive) - 운행 횟수에 연동

조수(Cleaner/Helper) 급여 옵션

행정/세금:

보험료 (연간)

도로세 (Road Tax): State Permit(TN주 내) vs National Permit(주간 이동) 선택 기능

피트니스 검사비 (FC Expenses)

관리비 (Admin Overhead): 매니저 인건비 배분 등

C. 운영 비용 (OPEX - Variable)

유류비: 첸나이 지역 디젤 단가, 차량 실연비(km/L)

소모품: 타이어 마모비(km당), 정비비(AMC/km당), 요소수(AdBlue) 비용

기타 잡비 (Incidentals):

톨게이트 비용 (FASTag)

RTO/Police/Loading Gate 관련 비공식 경비 (Trip당 혹은 km당 설정)

D. 시장 비교군 (Market Benchmark)

비교 기준 선택: Trip당 단가 / Km당 단가 / Ton당 단가 중 택 1

왕복 거리: 1 Trip 기준 주행 거리

3.2. 시뮬레이션 로직 (Simulation Logic)

EMI 계산: 원리금 균등 상환 방식 적용.

손익분기점(BEP) 분석: 자차 운영 비용이 외주 비용보다 저렴해지는 '월 최소 주행 거리' 산출.

민감도 분석 (Sensitivity Analysis): 주행거리 변화(X축)에 따른 자차 vs 외주 비용(Y축) 교차점 시각화.

단가 산출: CPK(Cost Per Km) 및 CPT(Cost Per Trip) 자동 계산.

3.3. 데이터 시각화 (Visualization)

Dashboard UI: 한 화면에서 입력과 결과를 동시에 확인 (Split View).

Charts:

비용 구성비 (Pie Chart): 유류비, 인건비, 금융비용 비중 확인.

BEP 그래프 (Line Chart): 거리별 원가 추이 비교.

손익 막대 (Bar Chart): 월간 예상 절감액 표시.

3.4. AI 어드바이저 (AI Analyst Feature)

Trigger: 사용자가 'AI 분석' 버튼 클릭 시 실행.

Role: 가상의 물류 컨설턴트 역할.

Logic (Rule-based AI):

판정 (Verdict): 절감액이 (+)면 "투자 적합", (-)면 "투자 주의/보류".

리스크 감지:

연료비 비중이 45% 초과 시 -> "연비 개선 교육 필요" 경고.

월 주행거리가 BEP 미달 시 -> "가동률(물동량) 확보 시급" 경고.

차량 노후화 대비 -> "3년차 이후 정비비 증가 고려" 조언.

Output: 대화형 텍스트 리포트 (판정 결과, 핵심 요약, 실행 제안 3단계 구성).

4. 비기능적 요구사항 (Non-Functional Requirements)

플랫폼: Web Base (HTML5/React) - 별도 설치 없이 브라우저 실행.

반응형 웹: PC 및 태블릿(iPad 등) 해상도 지원.

성능: 입력값 변경 시 0.5초 이내 실시간 재계산 (Real-time Calculation).

언어/통화:

UI 언어: 영어 (현지 직원 공유용) / 한국어 (본사 보고용) - 현재 버전은 혼용 또는 영어 권장

통화 단위: INR (₹) 표시. 1,00,000 (Lakh) 단위 표기 고려.

보안: 클라이언트 사이드(브라우저)에서만 동작하며, 입력 데이터가 외부 서버로 전송되지 않음.

5. 기술 스택 (Tech Stack)

Frontend: React.js (Single File Component 방식)

Visual Library: Recharts (차트 구현), Tailwind CSS (스타일링)

Icons: Phosphor Icons

6. 예상 산출물 (Deliverables)

Source Code: 단일 HTML 파일 (chennai_tco_simulator.html)

User Guide: 입력 변수 설명 및 결과 해석 가이드 (PDF/PPT)

7. 향후 확장성 (Future Roadmap)

데이터베이스 연동 (Firestore)을 통한 시뮬레이션 이력 저장.

실제 운행 데이터(GPS)와 연동하여 예측 정확도 보정.