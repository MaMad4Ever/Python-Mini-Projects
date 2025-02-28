import speedtest

def perform_speed_test():
   st = speedtest.Speedtest()
   servers = st.get_best_server()

   print("Testing download speed...")
   download_speed = st.download() / 1000000  # Convert to Mbps
   print("Testing upload speed...")
   upload_speed = st.upload() / 1000000  # Convert to Mbps

   return download_speed, upload_speed

if __name__ == "__main__":
   download_speed, upload_speed = perform_speed_test()
   print("Download Speed: {:.2f} Mbps".format(download_speed))
   print("Upload Speed: {:.2f} Mbps".format(upload_speed))
