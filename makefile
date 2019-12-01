solu.png : solu.dat
	python solu.py
	
	
solu.dat : solu.x
	./solu.x 10000 > solu.dat


solu.x : solu.cpp
	c++ solu.cpp -o solu.x


clean:
	rm solu.png solu.dat solu.x