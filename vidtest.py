import cv2 

Vid = cv2.VideoCapture(r'C:\Users\hspark02\Downloads\pexels-pavel-danilyuk-7318864.mp4')

if Vid.isOpened():
	fps = Vid.get(cv2.CAP_PROP_FPS)
	f_count = Vid.get(cv2.CAP_PROP_FRAME_COUNT)
	f_width = Vid.get(cv2.CAP_PROP_FRAME_WIDTH)
	f_height = Vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
	
	print('Frames per second : ', fps,'FPS')
	print('Frame count : ', f_count)
	print('Frame width : ', f_width)
	print('Frame height : ', f_height)

while Vid.isOpened():
	ret, frame = Vid.read()
	if ret:
		re_frame = cv2.resize(frame, (round(f_width/4), round(f_height/4)))
		cv2.imshow('Car_Video',re_frame)
		key = cv2.waitKey(10)
		
		if key == ord('q'):
			break
	else:
		break

Vid.release()
cv2.destroyAllWindows()