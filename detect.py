from ultralytics import YOLO

# Load YOLOv8 pre-trained model
model = YOLO("yolov8n.pt")

# Run detection on an image
results = model("https://ultralytics.com/images/bus.jpg", save=True)

print("Detection completed successfully!")
