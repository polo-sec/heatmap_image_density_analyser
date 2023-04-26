# heatmap_image_density_analyser
A simple tool to analyse heatmaps and plot both the percentage density of the Red, Yellow and Green highlighted areas, usually indicating the density of occurance for the measured factor. This allows reverse-engineering of the statistics used to create heatmaps on images that have already been overlayed with the result. 

# Usage

1. Install the dependencies with:

```
pip install -r requirements.txtk
```

2. Place the images inside of a 'Results' directory, in the same directory as the tool

3. Run the tool with

```
python3 heatmap_image_density_analyser.py
```

The results will be output on STDIN.
