 Google PAIR Mental Models: Notes for Human-Centered AI

## Source

Google People + AI Guidebook  
Chapter: Mental Models  
Link: https://pair.withgoogle.com/chapter/mental-models/

## Why this matters

This chapter is useful for understanding how users form expectations about AI systems.

A mental model is a user’s understanding of how a system works and how their actions affect it. In AI products, this becomes especially important because users may misunderstand what the system can and cannot do.

For example, in a finance assistant, a user may ask:

> Is this equity fund suitable for me?

The system may only be retrieving general educational content, but the user may assume the AI is giving personalised financial advice.

This mismatch can create risk.

---

## Key ideas from the chapter

### 1. AI systems need expectation-setting

AI systems can adapt, optimise, and personalise over time. Users need to understand what the AI can do, what it cannot do, and how its behaviour may change.

For a finance assistant, this means the interface should clearly say:

> This tool provides educational information. It does not provide personalised investment advice.

---

### 2. Users bring existing mental models

Users often understand new systems by comparing them with things they already know.

In finance, a user may compare an AI assistant with:

- A financial adviser
- A bank relationship manager
- A mutual fund distributor
- A personal finance journalist
- A search engine

Each comparison creates different expectations.

If the AI sounds confident and conversational, the user may wrongly assume it understands their full financial situation.

---

### 3. Onboarding should happen in stages

The chapter argues that AI products should not overload users with technical explanations at the beginning.

Instead, the system should explain:

- What the product does
- How it helps
- What it cannot do
- How the user can improve the output
- When the system may need more information

For a finance assistant, staged onboarding could look like:

> I can explain financial products in simple language.  
> I cannot tell you what to buy or sell without knowing your full financial situation.  
> For personalised advice, please consult a qualified adviser.

---

### 4. Explain the benefit, not the technology

Users do not need to know the technical details first.

Instead of saying:

> This system uses retrieval-augmented generation and embeddings.

A better user-facing explanation is:

> This assistant answers using selected educational sources and shows where the information came from.

This helps users build a clearer and safer mental model.

---

### 5. Plan for co-learning

AI systems and users can learn from each other over time.

The system may improve when users give feedback. But the interface should explain what feedback changes and what it does not change.

For example:

> Your feedback helps improve the clarity of future explanations. It does not make this answer personalised financial advice.

This distinction is important.

---

### 6. Avoid making AI seem too human

The chapter warns that human-like AI can create unrealistic expectations.

In finance, this is especially risky. A chatbot that says “I recommend this fund” may sound like a human adviser, even when it is only generating a general explanation.

Better wording:

> Based on the source provided, this fund has the following features and risks.

Avoid:

> I think this fund is right for you.

---

## Finance assistant example

### User goal

Understand whether an equity fund is suitable.

### System capability

Retrieve and explain general educational content about equity funds.

### User mental model

The user may think the AI is acting like a financial adviser.

### Risk of mismatch

The user may over-trust a generic answer and treat it as personalised investment advice.

### Interface intervention

The interface should:

- Show sources
- Add a limitation note
- Ask clarifying questions
- Explain risk factors
- Avoid buy/sell language
- Recommend professional advice for personalised decisions

Example interface message:

> I can explain how this equity fund works, but I cannot judge whether it is suitable for you without details such as your goals, time horizon, income, risk tolerance, and existing investments.

---

## Design checklist for my AI finance assistant

Before answering a finance query, the system should ask:

1. Is the user asking for education or advice?
2. Could the answer be mistaken as personalised advice?
3. Does the user know the system’s limits?
4. Are sources visible?
5. Is the answer using careful language?
6. Should the system ask clarifying questions?
7. Should a risk note be shown?
8. Is there an option to speak to a qualified adviser?

---

## My research takeaway

The main design challenge is not only whether the AI gives a correct answer.

The deeper question is:

> Does the user correctly understand what kind of answer they are receiving?

For human-centered AI in financial decision-making, mental models are central to trust, safety, and responsible interface design.
