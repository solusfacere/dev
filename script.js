// Global variables
let tasks = [];

// Function to add a task to the schedule
function addTask() {
    const taskName = document.getElementById('taskName').value;
    const taskDuration = parseInt(document.getElementById('taskDuration').value);

    tasks.push({ name: taskName, duration: taskDuration });
    updateChart();
}

// Function to update the pie chart
function updateChart() {
    const chartContainer = document.getElementById('chartContainer');

    // Calculate the total duration
    const totalDuration = tasks.reduce((total, task) => total + task.duration, 0);

    // Generate the data for the pie chart
    const chartData = tasks.map(task => {
        const percentage = (task.duration / totalDuration) * 100;
        return { y: percentage, label: task.name };
    });

    // Create the pie chart
    const chart = new CanvasJS.Chart(chartContainer, {
        animationEnabled: true,
        data: [{
            type: 'pie',
            startAngle: -90,
            dataPoints: chartData
        }]
    });

    // Render the chart
    chart.render();
}
