# sample execution (requires torchvision)
import torch
# Load the model from a file
model = torch.load("src/data/alexnet-pretrained.pt")
model.eval()
# Read the categories
with open("src/data/classes.txt", "r") as f:
	categories = [s.strip() for s in f.readlines()]
from torchvision import transforms
from flask import abort
import base64
import io
from PIL import Image
import numpy as np

class ServiceHandlers:

	# This method prepared domain data for a list of domain name
	@staticmethod
	def get_image(data):
		
		# print(request.json)      
		if not data or 'image' not in data: 
			abort(400)
				
		base64_decoded = base64.b64decode(data['image'])
		image = Image.open(io.BytesIO(base64_decoded))
		image_np = np.array(image)



		imageString = base64.b64decode(data['image'])

		#  convert binary data to numpy array
		nparr = np.fromstring(imageString, np.uint8)
		defa = np.asarray(nparr)
		#  let opencv decode image to correct format
		# img = cv2.imdecode(nparr, cv2.IMREAD_ANYCOLOR);
		# cv2.imshow("frame", img)
		# cv2.waitKey(0)

		# PIL image object to numpy array
		# img_arr = np.asarray(img)      
		# print('img shape', img_arr.shape)
		# convert bytes data to PIL Image object
		img = Image.open(io.BytesIO(imageString))

		return img

		# process your img_arr here    

	def process_image(data):
		input_image = ServiceHandlers.get_image(data)
		preprocess = transforms.Compose([
			transforms.Resize(256),
			transforms.CenterCrop(224),
			transforms.ToTensor(),
			transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
		])
		input_tensor = preprocess(input_image)
		input_batch = input_tensor.unsqueeze(0) # create a mini-batch as expected by the model

		# move the input and model to GPU for speed if available
		
		input_batch.to('cpu')
		model.to('cpu')

		with torch.no_grad():
			output = model(input_batch)
		# Tensor of shape 1000, with confidence scores over Imagenet's 1000 classes
		#print(output[0])
		# The output has unnormalized scores. To get probabilities, you can run a softmax on it.
		probabilities = torch.nn.functional.softmax(output[0], dim=0)
		print(probabilities)

		results = {}
		# Show top categories per image
		top5_prob, top5_catid = torch.topk(probabilities, 5)
		for i in range(top5_prob.size(0)):
			print(categories[top5_catid[i]], top5_prob[i].item())
			results[categories[top5_catid[i]]] = top5_prob[i].item()


		return results

