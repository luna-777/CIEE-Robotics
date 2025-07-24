from camera import Camera

filename = "cool_photo.png"
camera = Camera()

camera.start_image()
print("Saving image in...")
for i in range(10,0,-1):
	print(i)
result=camera.save_image(filename)
if result != None:
	print(f"Image saved tp {filename}")
camera.close()

