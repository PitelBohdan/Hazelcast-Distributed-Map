for i in 1 2 3 4 5 6 7 8 9 10; do
  curl -X POST http://localhost:5000/msg -d "msg$i"
done
