# use data_ingestion.py to ingest data and perform basic operations
from data_ingestion import ingest_csv
import matplotlib.pyplot as plt
from reporting import generate_report,convert_md_to_pdf
import seaborn as sns

app_path = r'C:\Users\WU425NK\OneDrive - EY\Desktop\Python_training\Capstone_Project\cap_app_inventory.csv'
compliance_path = r'C:\Users\WU425NK\OneDrive - EY\Desktop\Python_training\Capstone_Project\cap_compliance_status.csv'
def main():
    app_df = ingest_csv(app_path)  # Ingest app data
    compliance_df = ingest_csv(compliance_path)  # Ingest compliance data

    # merger the two dataframes on a common key (e.g., 'app_id')
    merged_df = app_df.merge(compliance_df, on='App_ID', how='left')
    
    if not merged_df.empty:
        print("Merged Data:")
        print(merged_df.head())  # Display the first few rows of the merged data
    else:
        print("No merged data available.")

    # Calculate the percentage of compliant status
    if 'Status' in merged_df.columns:
        compliance_percentage = (merged_df['Status'] == 'Compliant').mean() * 100
        print(f"Percentage of compliant applications: {compliance_percentage:.2f}%")
    else:
        print("Compliance status column not found in merged data.")

    # barchart of compliance score by department
    if 'Department' in merged_df.columns and 'Compliance_Score' in merged_df.columns:
        merged_df_sorted = merged_df.sort_values(by="Compliance_Score",ascending=True)
        #plt.figure(figsize=(10, 6))
        fig, ax = plt.subplots(figsize=(5, 5))
        sns.barplot(x='Department', y='Compliance_Score', data=merged_df_sorted,ax=ax)
        #plt.ylim(bottom=0)
        plt.title('Compliance Score by Department')
        plt.xticks(rotation=45)
        ax.set_ylim(0,5)
        ax.margins(y=0.15)
        plt.tight_layout()
        # plt.show()
        # save the plot in output directory
        plt.savefig('C:/Users/WU425NK/OneDrive - EY/Desktop/Python_training/Capstone_Project/compliance_score_by_department.png')

    else:
        print("Required columns for bar chart not found in merged data.")

    # Generate a report using the reporting module
    generate_report(
        filename='C:/Users/WU425NK/OneDrive - EY/Desktop/Python_training/Capstone_Project/compliance_report.md',
        summary_data='This report summarizes the compliance status of applications across departments.',
        compliance_data=merged_df[['App_Name', 'Department', 'Compliance_Score', 'Audit_Date']],
        compliance_percentage=compliance_percentage,
        chart_path='C:/Users/WU425NK/OneDrive - EY/Desktop/Python_training/Capstone_Project/compliance_score_by_department.png'
        #chart_path='../output/compliance_score_by_department.png'
    )

    # Convert the markdown report to PDF
    #markdown_to_pdf(markdown_file='C:/Users/WU425NK/OneDrive - EY/Desktop/Python_training/Capstone_Project/compliance_report.md', pdf_file='C:/Users/WU425NK/OneDrive - EY/Desktop/Python_training/Capstone_Project/compliance_report.pdf')
    convert_md_to_pdf(input_md_path='C:/Users/WU425NK/OneDrive - EY/Desktop/Python_training/Capstone_Project/compliance_report.md', output_pdf_path='C:/Users/WU425NK/OneDrive - EY/Desktop/Python_training/Capstone_Project/compliance_report.pdf')

if __name__ == "__main__":
    main()