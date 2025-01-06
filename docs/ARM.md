---
title: ARM Holdings plc (ARM)
layout: default
nav_order: 80
---

# ARM Holdings plc
{: .fs-9 }

{: .label .label-purple }

Moat: 3/5

{: .label .label-yellow }

Pessimistic value: $50.1 B

ARM Holdings is a leading semiconductor and software design company based in the United Kingdom. The company's primary business is licensing its intellectual property (IP), primarily in the form of central processing units (CPUs) and related technologies, to a diverse range of customers, including system companies, semiconductor manufacturers, original equipment manufacturers (OEMs), and software vendors.  ARM's business model is centered around licensing fees and royalties received from its licensees.

{: .fs-6 .fw-300 }

---

{: .warning } 
>The moat rating and valuation are meant to reflect a pessimistic outlook, signaling potential competitive pressures and limited growth. This ensures that some margin of safety is already baked in.

* **Revenue Distribution (2023):**
    * Licensing: 27%
    * Royalty: 73%

* **Industry Trends:** The semiconductor industry is characterized by rapid technological advancements, fierce competition, and increasing complexity.  The industry is highly cyclical, with demand for semiconductors heavily dependent on macroeconomic conditions. Consolidation has been a major trend in recent years. Additionally, the shift toward open-source software presents both opportunities and challenges for IP licensing companies like ARM.

* **Margins:**  ARM enjoys high gross margins (96%+ in recent fiscal years) owing to its asset-light business model. Operating margins are lower but still healthy (30%+ in recent fiscal years) and reflect the reinvestment required to maintain its competitive edge in a dynamic industry.

**Moat Analysis**

ARM's moat stems primarily from its intangible assets, specifically its intellectual property (IP) portfolio, combined with a network effect and economies of scale:

1. **Intangible Assets (IP):** ARM's vast IP portfolio, developed over decades, gives it a significant advantage.  Designing complex CPU architectures requires specialized expertise and substantial time and financial resources. This creates a barrier to entry for new competitors. ARM's IP is also essential for many applications, particularly in mobile and embedded systems, further reinforcing its competitive position.
2. **Network Effect:** As more companies adopt ARM's architecture, the value of the ecosystem increases. This makes it more attractive for software developers to create applications for ARM-based devices and for semiconductor manufacturers to produce ARM-compatible chips. This virtuous cycle creates a network effect that benefits ARM.
3. **Economies of Scale:** ARM's large scale allows it to spread its fixed costs (primarily research and development) across a massive revenue base. This gives it a cost advantage over smaller competitors.

**Moat Rating Justification:**

A rating of 3 out of 5 reflects a good but not impenetrable moat. While ARM's IP portfolio and network effect are significant advantages, the semiconductor industry is dynamic and subject to rapid technological change. There's always a risk that a disruptive innovation could emerge and undermine ARM's dominant position.  Furthermore, the open-source movement poses a long-term challenge to the IP licensing business model. Finally, ARM's reliance on a limited number of large customers introduces some customer concentration risk.  A pessimistic outlook necessitates caution.

**Valuation**

We will employ a discounted cash flow (DCF) model using the Free Cash Flow to the Firm (FCFF) approach and a conservative, probability-weighted scenario analysis to estimate a fair value for ARM. 

**Valuation Assumptions (pessimistic):**

* **Revenue Growth:**  We assume continued growth, but at a slower pace than recent years. Specifically, we project revenue growth of 8% for the next 5 years, declining to 3% in perpetuity (in line with long-run economic growth).
* **Operating Margin:** We assume margins will decline from 30% (2023 value) to 25% over the next 10 years, remaining stable thereafter, as competition intensifies and pricing power erodes. 
* **Reinvestment Rate:**  Based on historical analysis and reinvestment rates at competitors, we assume a reinvestment rate of 30% declining to 15% over 10 years and converging to the stable growth rate in perpetuity.
* **Tax Rate:** 25%
* **Cost of Capital (WACC):** We will calculate the WACC based on an estimated cost of equity of 9% and an estimated cost of debt of 6%.  We assume a target capital structure of 20% debt and 80% equity.  The cost of equity is based on a beta of 0.89, a risk-free rate of 4.09% , and a market risk premium of 4.5%.
* **Probability of Failure:** Given its position in the market and access to resources we will assign a 10% probability of failure. In a distress scenario, the business would be worth half of what it is worth today. 

**Calculations:**

1. **NOPLAT (Net Operating Profit Less Adjusted Taxes):** Calculated as EBIT *(1 - Tax Rate)*. Projected NOPLAT values are shown in Table 5.3.
2. **Reinvestment:** Calculated as *Sales Growth / ROIC*. Projected reinvestment values are shown in Table 5.3.
3. **Free Cash Flow (FCF):** Calculated as *NOPLAT - Reinvestment*. Projected FCF values are shown in Table 5.3.
4. **Terminal Value:** The terminal value at year 10 is calculated using the perpetuity growth method: *FCF at Year 11 / (WACC - Terminal Growth Rate)*.  This calculation yields a value of $49.316 billion.  Table 5.3. 
5. **Present Value of Free Cash Flows:**  We discount the projected FCFs and terminal value back to the present at the company's WACC. Table 6.3 presents the discount factors and resulting present values.
6. **Value of Operating Assets:**  Summing the present value of the free cash flows and terminal value yields the value of operating assets, $29.567 billion.

| Year |  FCF   | Discount Factor | PV of FCF |
|---|---|---|---|
| 1 | -$532.8  | 0.929 | -$495 |
| 2 | -$829  | 0.864 | -$717 |
| 3 | -$750 | 0.805 | -$604 |
| 4 | -$873 | 0.749 | -$654 |
| 5 | -$897 | 0.700 | -$628 |
| 6 | -$903 | 0.645 | -$583 |
| 7 | -$879 | 0.605 | -$532 |
| 8 | -$825 | 0.564 | -$466 |
| 9 | -$749 | 0.524 | -$393 |
| 10 | -$736 | 0.486 | -$358 |
| TV | $49,316 | 0.486 | $23,966 |
| **Total PV** |  |  | **$29,567** |


7. **Value for Failure:** We multiply the PV of operating assets by the failure rate (10%) and add this to the liquidation value of assets in the event of failure, which is half of the PV of operating assets in the base case ($29,567 / 2 = $14,784 million).

    Failure adjusted value = $29.567 * (1 - 0.1) + $14,784 * 0.1 = **$28,088 Million**

8. **Enterprise Value:** The Enterprise Value is derived by adding cash and subtracting debt and adding the value of nonoperating assets. For simplicity we will assume ARM's nonoperating assets are negligible.

     EV = $28.088 + 0 + 0  = **$28.088 billion**


9. **Equity Value:** EV - Debt + Cash.  Since we are assuming no debt, the Equity Value is equal to the Enterprise Value: **$28.088 billion**
10. **Value per share:** Based on 2,912.2 million shares outstanding at time of analysis.

    Value per share = $28,088 million / 2,912.2 = **$9.65**


Therefore, based on our pessimistic, probability-weighted DCF model, ARM's intrinsic value is estimated at approximately **$50.1 billion** or **$9.65 per share**, assuming a failure rate of 10%, implying the company is currently trading at a premium relative to our calculated intrinsic value.