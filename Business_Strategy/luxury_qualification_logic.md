# 📋 Luxury Real Estate Lead Qualification Logic (v1.0)

## 🎯 Goal
Transform a raw inquiry into a "Deal-Ready" lead by verifying financial capability, urgency, and specific luxury requirements, ensuring human agents only spend time on high-probability closings.

## 🛠️ Qualification Workflow (The Logic Tree)

### Step 1: Interest & Intent (The Hook)
- **Objective**: Identify the specific property or "vibe" they are seeking.
- **Key Questions**: 
    - "Which property in our portfolio caught your eye?"
    - "Are you looking for a primary residence or an investment asset?"
- **Exit Criteria**: Lead provides a specific property name or a clear set of luxury requirements (e.g., "Oceanfront in Malibu").

### Step 2: Financial Validation (The Filter)
- **Objective**: Ensure the buyer has the liquidity for a luxury transaction.
- **Key Questions**: 
    - "To ensure we prioritize the right options, what is your target budget range for this acquisition?"
    - "Will this be a cash purchase, or are you utilizing a pre-approved mortgage?"
- **High-End Signal**: Requesting a "Proof of Funds" (POF) or "Bank Comfort Letter" for properties over \$5M.
- **Exit Criteria**: Budget aligns with the property price + Financing method is confirmed.

### Step 3: Timeline & Urgency (The Velocity)
- **Objective**: Distinguish between "window shoppers" and "serious buyers".
- **Key Questions**: 
    - "Are you looking to close within the next 30 days, or are you planning for a longer-term transition (3-6 months)?"
    - "Do you have a hard deadline for moving in (e.g., school year, tax cycle)?"
- **Exit Criteria**: Timeline is explicit.

### Step 4: Friction & Logistics (The Final Check)
- **Objective**: Remove all operational hurdles before the human agent steps in.
- **Key Questions**: 
    - "Do you have your pre-approval letter or proof of funds ready for a priority tour?"
    - "Who else is involved in the decision-making process (e.g., spouse, family office, lawyer)?"
- **Exit Criteria**: Readiness for tour is confirmed.

## 🚀 "Deal-Ready" Definition
A lead is marked **DEAL-READY** if and only if:
1. **Property** is identified.
2. **Budget** is confirmed $\ge$ Property Price.
3. **Financing** is verified (Cash/Pre-approved).
4. **Timeline** is defined.
5. **POF/Pre-approval** is ready for submission.

## 📈 Implementation Note for AI Agent
The agent should use "Soft-Closing" language. Instead of "I need your bank statement," use "To ensure we can secure a priority viewing for you, most of our high-end clients provide a proof of funds upfront."
