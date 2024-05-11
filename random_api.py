from fastapi import FastAPI
import random


jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why did the math book look sad? Because it had too many problems!",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "Why don't eggs tell jokes? They'd crack each other up!",
    "What do you call a fake noodle? An Impasta!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why did the kid throw his clock out the window? To see time fly!",
    "What do you call a boomerang that doesn't come back? A stick!",
    "Why didn't the melons get married? Because they cantaloupe!",
    "Why did the kid throw his clock out the window? To see time fly!",
    "What did one wall say to the other wall? I'll meet you at the corner!",
    "What did one toilet say to the other toilet? You look a bit flushed!",
    "Why did the kid throw his clock out the window? To see time fly!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the math book look sad? Because it had too many problems!",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "Why don't eggs tell jokes? They'd crack each other up!",
    "What do you call a fake noodle? An Impasta!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "What do you call a boomerang that doesn't come back? A stick!",
    "Why didn't the melons get married? Because they cantaloupe!",
    "What did one wall say to the other wall? I'll meet you at the corner!",
    "What did one toilet say to the other toilet? You look a bit flushed!",
    "Why did the kid throw his clock out the window? To see time fly!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't scientists trust atoms? Because they make up everything!"
]

quotes = [
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough. - Oprah Winfrey",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The best way to predict the future is to create it. - Peter Drucker",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Happiness is not something ready-made. It comes from your own actions. - Dalai Lama",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough. - Oprah Winfrey",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The best way to predict the future is to create it. - Peter Drucker",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Happiness is not something ready-made. It comes from your own actions. - Dalai Lama",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough. - Oprah Winfrey",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The best way to predict the future is to create it. - Peter Drucker",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Happiness is not something ready-made. It comes from your own actions. - Dalai Lama",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough. - Oprah Winfrey"
]

facts = [
    "The tallest mammal on Earth is the giraffe.",
    "The first product to have a barcode was Wrigley's gum.",
    "Apples are more effective at waking you up in the morning than coffee.",
    "The world's smallest mammal is the bumblebee bat, which is about the size of a thumb.",
    "Bananas are slightly radioactive.",
    "The largest known prime number has 23,249,425 digits.",
    "Chocolate has a longer shelf life when stored at room temperature than when refrigerated.",
    "The first product to have a barcode was Wrigley's gum.",
    "Apples are more effective at waking you up in the morning than coffee.",
    "The world's smallest mammal is the bumblebee bat, which is about the size of a thumb.",
    "Bananas are slightly radioactive.",
    "The largest known prime number has 23,249,425 digits.",
    "Chocolate has a longer shelf life when stored at room temperature than when refrigerated.",
    "The first product to have a barcode was Wrigley's gum.",
    "Apples are more effective at waking you up in the morning than coffee.",
    "The world's smallest mammal is the bumblebee bat, which is about the size of a thumb.",
    "Bananas are slightly radioactive.",
    "The largest known prime number has 23,249,425 digits.",
    "Chocolate has a longer shelf life when stored at room temperature than when refrigerated.",
    "The first product to have a barcode was Wrigley's gum.",
    "Apples are more effective at waking you up in the morning than coffee.",
    "The world's smallest mammal is the bumblebee bat, which is about the size of a thumb.",
    "Bananas are slightly radioactive.",
    "The largest known prime number has 23,249,425 digits.",
    "Chocolate has a longer shelf life when stored at room temperature than when refrigerated.",
    "The first product to have a barcode was Wrigley's gum.",
    "Apples are more effective at waking you up in the morning than coffee.",
    "The world's smallest mammal is the bumblebee bat, which is about the size of a thumb.",
    "Bananas are slightly radioactive.",
    "The largest known prime number has 23,249,425 digits."
]

app = FastAPI()


@app.get("/jokes")
async def read_user_item():
    return random.choice(jokes)

@app.get("/quotes")
async def read_user_item():
    return random.choice(quotes)

@app.get("/facts")
async def read_user_item():
    return random.choice(facts)