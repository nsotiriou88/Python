package main

import (
	"fmt"
	"time"

	"github.com/Arafatk/glot"
)

func main() {
	dimensions := 2
	// The dimensions supported by the plot
	persist := false
	debug := false
	plot, _ := glot.NewPlot(dimensions, persist, debug)
	pointGroupName := "Simple Circles"
	style := "circle"
	points := [][]float64{{7, 3, 13, 5.6, 11.1}, {12, 13, 11, 1, 7}}
	// Adding a point group
	plot.AddPointGroup(pointGroupName, style, points)

	//Add 4 points
	pointGroupName = "Simple Lines"
	style = "lines"
	points = [][]float64{{7, 3, 3, 5.6, 5.6, 7, 7, 9, 13, 13, 9, 9}, {10, 10, 4, 4, 5.4, 5.4, 4, 4, 4, 10, 10, 4}}
	plot.AddPointGroup(pointGroupName, style, points)

	// A plot type used to make points/ curves and customize and save them as an image.
	plot.SetTitle("Example Plot")
	// Optional: Setting the title of the plot
	plot.SetXLabel("X-Axis")
	plot.SetYLabel("Y-Axis")
	// Optional: Setting label for X and Y axis
	plot.SetXrange(-2, 18)
	plot.SetYrange(-2, 18)
	// Optional: Setting axis ranges
	plot.SavePlot("2.png")

	fmt.Println(5 + float64(time.Now().Nanosecond())/1000000000)
	fmt.Println(float64(time.Now().Hour() * 10000))
	fmt.Println((float64(time.Now().Hour()*10000) + float64(time.Now().Minute()*100) + float64(time.Now().Second()) + float64(time.Now().Nanosecond())/1000000000))

	var coco float64
	x := time.Now().UnixNano()
	y := time.Now().Unix()
	coco = float64(x) / 1000000000.0
	fmt.Println(coco, y)

}
