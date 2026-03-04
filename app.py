import streamlit as st
st.title("Prilojenie")
if "books" not in st.session_state:
 st.session_state.books = []
st.header("Dobavi kniga")
title = st.text_input("Zaglavie")
author = st.text_input("Avtor")
price = st.number_input("Cena", min_value = 0)
if st.button("Dobavi knigata"):
  book = {
    "title": title,
    "author": author,
    "price": price
  }
  st.session_state.books.append(book)
  st.success("Knigata e dobavena")
 if st.button ("Pokaji vsichki knigi"):
  if len(st.session_state.books) == 0:
    st.write("Nqma dobaveni knigi")
 else:
   for book in st.session_state.books:
    st.write("Zaglavie:", book["title"])
    st.write("Avtor:", book["author"])
    st.write("Cena:", book[price])
    st.write("-----------------")
st.header("Tursene po avtor")
search_author = st.text_input("Vuvedi ime na avtor")
if st.button("Tursi po avtor"):
  found = False
for book in st.session_state.books:
 if book["author"] == search.author:
  st.write(book)
  found = True
 if found == False:
    st.write("Nqma namereni knigi ot tozi avtor")
