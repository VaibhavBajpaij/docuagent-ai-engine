import sys
import os

# Add root directory to sys.path so src imports resolve cleanly in Vercel Serverless environment
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.app import app
