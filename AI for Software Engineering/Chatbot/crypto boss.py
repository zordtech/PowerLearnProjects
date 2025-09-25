def greet():
    print("🤖 Crypto Boss: Hey there! Let’s find you a green and growing crypto! 💹")
   
crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    }  
}

def crypto_boss_brain(user_query):
    user_query = user_query.lower()

    if "sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"🌱 Invest in {recommend}! It’s eco-friendly and has long-term potential!"

    elif "trending" in user_query or "rising" in user_query:
        trending = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
        return f"📈 These coins are trending up: {', '.join(trending)}"

    elif "long-term" in user_query or "growth" in user_query:
        # prioritize rising + high market cap
        best = [coin for coin, data in crypto_db.items() 
                if data["price_trend"] == "rising" and data["market_cap"] == "high"]
        if best:
            return f"🚀 For long-term growth, consider {best[0]} — strong growth potential!"
        else:
            return "🤔 Hmm… none match long-term growth perfectly right now."

    else:
        return "🤖 Sorry, I didn’t understand. Try asking about sustainability or trending coins."
        
def chat():
    greet()
    print("💬 Type 'exit' to end the chat.\n")

    while True:
        user_query = input("You: ")
        if user_query.lower() == "exit":
            print("👋 Crypto Boss: Remember, crypto is risky — always do your own research!")
            break

        response = crypto_boss_brain(user_query)
        print("Crypto Boss:", response)

print("\n⚠️ Disclaimer: Crypto investments are risky. This bot is for educational purposes only!")
        
if __name__ == "__main__":
    chat()
