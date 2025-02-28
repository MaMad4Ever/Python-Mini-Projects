from rembg import remove 
from PIL import Image 
  
input_path = './image.png' 
  
output_path = './Remove-BG.png' 
  
input = Image.open(input_path) 

output = remove(input) 
  
output.save(output_path)
