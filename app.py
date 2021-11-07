import streamlit as st
import pickle
from datetime import datetime
startTime = datetime.now()
# import znanych nam bibliotek

filename = "model.sv"
model = pickle.load(open(filename,'rb'))
# otwieramy wcześniej wytrenowany model

illnesses_d = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5"}
causes_d = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5"}
# o ile wcześniej kodowaliśmy nasze zmienne, to teraz wprowadzamy etykiety z ich nazewnictwem
def main():

	st.set_page_config(page_title="Czy pacjent przeżyje tydzień...?")
	overview = st.container()
	left, right = st.columns(2)
	prediction = st.container()

	st.image("https://media1.popsugar-assets.com/files/thumbor/7CwCuGAKxTrQ4wPyOBpKjSsd1JI/fit-in/2048xorig/filters:format_auto-!!-:strip_icc-!!-/2017/04/19/743/n/41542884/5429b59c8e78fbc4_MCDTITA_FE014_H_1_.JPG")

	with overview:
		st.title("Czy pacjent przeżyje tydzień...?")

	with left:
		illnesses_radio = st.radio( "Choroby współistniejące", list(illnesses_d.keys()), format_func=lambda x : illnesses_d[x] )
		causes_radio = st.radio("Objawy", list(causes_d.keys()), format_func=lambda x: causes_d[x] )

		with right:
			age_slider = st.slider("Wiek", value=50, min_value=1, max_value=100)
			height_slider = st.slider( "Wzrost", value=180, min_value=100, max_value=250)

	data = [[causes_radio, age_slider, illnesses_radio, height_slider]]
	survival = model.predict(data)
	s_confidence = model.predict_proba(data)

	with prediction:
		st.header("Czy dany pacjent przeżyje tydzień? {0}".format("Tak" if survival[0] == 0 else "Nie"))
		st.subheader("Pewność predykcji {0:.2f} %".format(s_confidence[0][survival][0] * 100))

if __name__ == "__main__":
    main()

## Źródło danych [https://www.kaggle.com/c/titanic/](https://www.kaggle.com/c/titanic), zastosowanie przez Adama Ramblinga