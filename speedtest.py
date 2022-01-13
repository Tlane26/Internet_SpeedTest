from speedtest import Speedtest

st = Speedtest();

print("Conection's Download speed is:", st.download())
print("Conection's Upload speed is:", st.upload())