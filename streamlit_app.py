import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# --- Seiteneinstellungen ---
st.set_page_config(page_title="📈 Dividenden Tracker", layout="wide")

# --- Titel ---
st.title("📊 Dividenden Tracker")
st.write("Willkommen zu deinem Dividenden-Tracker mit Streamlit + yFinance 🚀")

# --- Beispiel-Aktie (Apple) ---
ticker_symbol = "AAPL"  # Apple als Test

st.subheader(f"Aktienkurs von {ticker_symbol}")
ticker = yf.Ticker(ticker_symbol)

# Kursdaten laden
hist = ticker.history(period="1y")

# --- Linie zeichnen ---
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(hist.index, hist["Close"], label="Schlusskurs")
ax.set_ylabel("Preis in USD")
ax.set_title(f"Verlauf der letzten 12 Monate: {ticker_symbol}")
ax.legend()
st.pyplot(fig)

# --- Dividenden-Daten anzeigen ---
st.subheader("Dividendenzahlungen")
dividends = ticker.dividends

if dividends.empty:
    st.info("Keine Dividenden gefunden.")
else:
    df = dividends.reset_index()
    df.columns = ["Datum", "Dividende"]
    st.dataframe(df)
# === Kursdaten laden ===
data = ticker.history(period="1y")

# === Chart anzeigen ===
st.line_chart(data["Close"])

# === Dividenden anzeigen ===
if "Dividends" in data.columns:
    st.subheader("📈 Ausgeschüttete Dividenden")
    st.bar_chart(data["Dividends"])
else:
    st.write("Keine Dividenden-Daten verfügbar.")
