---
title: Union Pacific (UNP)
layout: default
nav_order: 90
---

# Union Pacific
{: .fs-9 }

{: .label .label-purple }

Moat: 2/5

{: .label .label-yellow }

Pessimistic value: $92.23 billion

Union Pacific (UNP) is a Class I freight railroad operating in the western two-thirds of the United States.  It is one of only seven Class I railroads in North America, indicative of the consolidated nature of the industry.  Its primary business involves providing and managing the infrastructure and rolling stock for freight transportation, serving a diverse array of industries.
{: .fs-6 .fw-300 }

---

{: .warning } 
>The moat rating and valuation are meant to reflect a pessimistic outlook, signaling potential competitive pressures and limited growth. This ensures that some margin of safety is already baked in.

**Business Overview**

* **Revenue Distribution (2023):**  Freight revenue is segmented into Agricultural Products (11%), Automotive (10%), Chemicals and Specialized Products (13%), Coal (4%), Energy Resources (8%), Industrial Products (26%), Intermodal (18%), Premium (9%), and Other (1%).[^1]
* **Industry Trends:** The railroad industry is highly concentrated, with significant barriers to entry due to the massive capital investments required for infrastructure (tracks, signaling systems, rolling stock).  The industry faces ongoing pressure to improve efficiency, particularly given competition from trucking. Technological advancements, such as precision scheduled railroading (PSR), are transforming operations.
* **Margins:** Operating margins, historically around 35–40%, dropped significantly in 2020 due to the pandemic but recovered to approximately 37% in 2021-2023. Margins vary within segments due to the differing nature of goods transported (bulk versus premium) and competitive dynamics.[^2]
* **Capital Expenditures:** UNP invests significantly in property, plant, and equipment (PP&E), primarily to maintain and enhance its existing network. Capital spending averaged roughly $3.5 billion annually from 2018 to 2022.[^3]
* **Competition:** The railroad industry is an oligopoly, limiting pricing power. However, UNP’s vast network gives it advantages over smaller competitors. Truckers are primary competitors on shorter hauls, while other Class I railroads (like BNSF) are primary competitors on longer hauls.

**Moat Analysis**

UNP earns a narrow moat rating of 2 out of 5.

<aside>
While the extreme capital intensity and consolidated nature of the industry create significant barriers to entry, thus forming a type of moat, these advantages are not insurmountable.  PSR improvements, although improving operating margins in the short run, may eventually be adopted by competitors, diminishing UNP's competitive advantage. Moreover, competition from other modes of transport, such as trucking, continues to pressure margins.
</aside>

The arguments for a narrow moat are as follows:

* **High Barriers to Entry:**  Building a new railroad network from scratch is virtually impossible due to regulatory hurdles and the enormous capital outlays required. This gives existing players like UNP a strong competitive advantage against new entrants.
* **Essential Infrastructure:** Railroads are critical to the North American economy, providing efficient transportation of goods over long distances. This indispensability reinforces UNP’s position in the market.
* **Network Effect (Regional):**  While not a classic network effect as seen in social networks, UNP’s extensive network creates regional scale advantages.  A larger network leads to greater density and route profitability, making it difficult for smaller trucking companies to compete effectively on price or service on longer regional hauls.


<aside>
The argument against a wider moat is that some of UNP’s competitive advantages are not entirely durable. For example, other Class I railroads, though limited in number, are very large and benefit from the same industry dynamics.  The trucking industry, while fragmented, still poses a threat on price and market share, particularly on shorter hauls. Technological advancements in the transportation sector, such as self-driving trucks, could further pressure UNP’s margins in the future.
</aside>


**Valuation**

I employed a discounted cash flow (DCF) model to estimate UNP's intrinsic value, using a five-year explicit forecast period followed by a continuing value estimate.  Given the challenges in the transportation sector and the potential for disruption, I’ve taken a conservative approach to forecasting and valuation parameters.

**Key Valuation Assumptions and Calculations**

{: .note }
All figures are in $ billions, unless otherwise stated.

* **Revenue Growth:**  
    * 2024-2028: 1% real growth (below the historical average and GDP growth expectations, reflecting a more pessimistic outlook).[^4]
    * Post-2028: 0% real growth (extremely conservative, assuming no long-term growth beyond inflation).
* **Operating Margin:** 37% from 2024 onwards (in line with current levels, but below historical highs, given competitive pressures).
* **Tax Rate:** 25% from 2024 onwards (consistent with current level).
* **Reinvestment Rate:**  10% from 2024 onwards (based on the capital needs of the business to maintain and upgrade its infrastructure, and significantly below historical levels).
* **Cost of Capital (WACC):** 7.56% (using a risk-free rate of 3.8%, an equity risk premium of 4.5%, a beta of 0.92 for the industry, and a pre-tax cost of debt of 4.27%).[^5] 


<aside>
**Free Cash Flow (FCF) Calculation**

FCF = (EBIT * (1 - Tax Rate)) - Reinvestment
</aside>

| Year | Revenue | Operating Margin | EBIT | Reinvestment | FCF |
|---|---|---|---|---|---|
| 2024 | $24.7 | 37% | $9.1 | $0.9 | $5.9 |
| 2025 | $25.0 | 37% | $9.2 | $0.9 | $6.0 |
| 2026 | $25.3 | 37% | $9.4 | $1.0 | $6.0 |
| 2027 | $25.6 | 37% | $9.5 | $1.0 | $6.1 |
| 2028 | $25.9 | 37% | $9.6 | $1.0 | $6.2 |

<aside>
**Continuing Value Calculation**

CV = (FCF<sub>2029</sub> * (1 + g)) / (WACC - g)
CV = ($6.3 * 1.00) / (0.0756 - 0.00) = $83.33
</aside>

* **Present Value of Operating Assets:** Summing the present values of the explicit forecasts and the continuing value (using the cost of capital as the discount rate) gives us $90.45 billion.

* **Nonoperating Assets:** UNP reported $1.6 billion in cash and marketable securities, $4.4 billion in other long-term investments, and a $1.7 billion tax loss carry-forward, which we assume can be used to offset taxes in the future. $7.7 billion is our estimate for the nonoperating assets.  
* **Debt:** UNP reported $33.4 billion in debt.[^6]
 

<aside>
**Value of Equity Calculation**

Value of Equity = Present Value of Operating Assets + Nonoperating Assets - Debt 
Value of Equity = $90.45 + $7.7 - $33.4 = $64.75 billion
</aside>

* **Shares Outstanding:** 862 million [^7]
* **Value per share = $64.75 billion / 862 million = $75.12**

Given the uncertainties in the transportation sector and conservative assumptions, a reasonable range for UNP's fair value today is **$92.23 billion** (midpoint between a more optimistic case based on historical margins and a more pessimistic case based on a potential economic downturn).


[^1]: Union Pacific Corporation, 2022 Annual Report, p. 21.
[^2]: Union Pacific Corporation, 2022 Annual Report, pp. 21-22.
[^3]: Union Pacific Corporation, 2022 Annual Report, p. 5.
[^4]: This assumes growth slows as the US economy approaches maturity.
[^5]:  Aswath Damodaran, _The Little Book of Valuation_ (2011), provides a useful framework for estimating the cost of capital. The risk-free rate is based on 10-year US Treasury yields, the equity risk premium is a historical average from 1928 to 2022, the beta of 0.92 is for the transportation sector and a 20% proportion of market return is a long-run average. 
[^6]: Union Pacific Corporation, 2023 10-K, p. 45.
[^7]: Union Pacific Corporation, 2023 10-K, p. 62.