# 🤖 Car Purchase Prediction using Bayesian Belief Network

This project uses a simple **Bayesian Belief Network** to predict whether a person will buy a car based on their **income** and **age**.

---

## 🔁 Bayesian Network Structure

- Nodes: `Income`, `Age`, `BuysCar`
- Edges: `Income → BuysCar`, `Age → BuysCar`
- Model implemented using `pgmpy`

---

## 📊 Conditional Probabilities

### Income:
- Low: 60%
- High: 40%

### Age:
- Young: 50%
- Old: 50%

### BuysCar (given Income & Age):

| Income | Age | P(Buys=Yes) |
|--------|-----|-------------|
| Low    | Young | 0.1       |
| Low    | Old   | 0.3       |
| High   | Young | 0.4       |
| High   | Old   | 0.8       |

---

## 🧪 Inference

We predict the **probability of buying a car** for a person with:

- Income = High
- Age = Young

Sample Output:
```
+-----------+--------------+
| BuysCar   | phi(BuysCar) |
+===========+==============+
| BuysCar_0 |       0.6    |
| BuysCar_1 |       0.4    |
+-----------+--------------+
```

---

## 💻 How to Run

1. Install dependencies:
   ```bash
   pip install pgmpy
   ```

2. Run the script:
   ```bash
   python bayesian_belief_network.py
   ```

---

## 🛠️ Hardware Implementation Idea

This Bayesian model can power a **voice assistant** in car showrooms:
- Collects verbal inputs (e.g., “I’m 25 and earn well”)
- Internally maps these to `Age`, `Income`
- Runs Bayesian inference to suggest cars or offers
- Runs on Raspberry Pi + microphone module

---

## 📁 Files

- `bayesian_belief_network.py` – Code to define and run the Bayesian network
- `README.md` – Project overview

---

## 🔖 License

This project is for academic and learning purposes only.