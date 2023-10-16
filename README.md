# Uber-Data-Engineering-Project-with-GCP-Modern-Tools
Developed a modern data engineering project on the Uber dataset using Google Cloud Platform (GCP). Built a data model in fact and dimension format, transformed the data using Python, deployed the code on a compute instance, loaded the data onto BigQuery, and created a final dashboard for data analysis and visualization.
# Steps Involved in the Project
1._**Create Bucket:**_ Create a storage bucket in GCP to store the project files.

2._**Create Instance**_: Set up a GCP compute instance with the following specifications:
  CPU: e2 standard 16
  8 core CPU
  64 GB RAM
  
3._**SSH Connection**_: Establish an SSH connection to the GCP compute instance.

4._**Run Command**_: Execute the commands provided in the command.txt file from the GitHub repository to install Python3 and the required libraries, including:
  **pandas
    mage.ai
    Google Cloud SDK**
  
5._**Start Mage.ai Project**_: Launch the Maze.ai project on port 6789 and access it through the external IP provided by the GCP instance.

6._**Update Firewall Rule**_: Modify the firewall rule to allow access to the Maze.ai dashboard via the external IP and port.

7._**Create Data Loader Pipeline**_: Set up a data loading pipeline to import the Uber dataset into the project.

8._**Create Data Transformer Pipeline**_: Develop a data transformation pipeline using a generic template. Handle any errors or kernel overloads that may occur during the transformation process.

9._**Connect to DataExporter**_: Connect the data transformation pipeline to the DataExporter module to export the transformed data to Google BigQuery.

10._**Configure io_config.yaml**:_ Access GCP, open API services, and create a new service account. Download the service account key in JSON format and copy the JSON data into the io_config.yaml file. This step ensures secure access to GCP services.

11._**Complete Data Loader Pipeline**_: After completing the third pipeline, navigate to BigQuery and refresh the data to preview the connected data.

12._**Data Visualization**_: Utilize Looker or Data Studio to create visualizations and analyze the Uber dataset.
# Dependencies for the Project
  -pandas

  -mage.ai
  
  -Google Cloud SDK
  
  -Google Cloud BigQueryroject
# License
This project is licensed under the [MIT License](LICENSE).

