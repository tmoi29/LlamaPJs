tab_gen:
	rm *.db
	python db_builder.py

run:
	rm *.db
	python db_builder.py
	python stu_mean.py
