#!/usr/bin/env python3
import pypdf
import os

def create_properly_numbered_chapters():
    """Create properly numbered chapters with correct boundaries and clear naming"""
    
    # Final structure with separated Notation and clear chapter numbering
    chapters = [
        ("00_Notation", 13, 14),   # Notation section only (reduced by 2 pages)
        ("01_Part_One_Prelude", 15, 32),   # Part One Prelude (starts 2 pages earlier)
        ("02_Ch01_Factor_Graphs_for_SLAM", 33, 65),  # Chapter 1
        ("03_Ch02_Advanced_State_Variable_Representations", 66, 85),  # Chapter 2
        ("04_Ch03_Robustness_to_Incorrect_Data_Association_and_Outliers", 86, 111),  # Chapter 3
        ("05_Ch04_Differentiable_Optimization", 112, 129),  # Chapter 4
        ("06_Ch05_Dense_Map_Representations", 130, 159),  # Chapter 5
        ("07_Ch06_Certifiably_Optimal_Solvers_and_Theoretical_Properties", 160, 192),  # Chapter 6 (reduced by 2 pages)
        ("08_Part_Two_Prelude", 193, 202),  # Part Two Prelude (starts 2 pages earlier)
        ("09_Ch07_Visual_SLAM", 203, 233),  # Chapter 7
        ("10_Ch08_LiDAR_SLAM", 234, 259),  # Chapter 8  
        ("11_Ch09_Radar_SLAM", 260, 291),  # Chapter 9
        ("12_Ch10_Event_based_SLAM", 292, 312),  # Chapter 10
        ("13_Ch11_Inertial_Odometry_for_SLAM", 313, 341),  # Chapter 11
        ("14_Ch12_Leg_Odometry_for_SLAM", 342, 369),  # Chapter 12
        ("15_Ch13_Boosting_SLAM_with_Deep_Learning", 370, 399),  # Chapter 13
        ("16_Ch14_Map_Representations_with_Differentiable_Volume_Rendering", 400, 420),  # Chapter 14
        ("17_Ch15_Dynamic_and_Deformable_SLAM", 421, 456),  # Chapter 15
        ("18_Ch16_Metric_Semantic_SLAM", 457, 491),  # Chapter 16
        ("19_Ch17_Towards_Open_World_Spatial_AI", 492, 522),  # Chapter 17
        ("20_Ch18_The_Computational_Structure_of_Spatial_AI_Systems", 523, 553),  # Chapter 18
        ("21_References", 554, 646),  # References section
    ]
    
    return chapters

def split_pdf_final(input_pdf_path, output_dir):
    """Split PDF with final corrected boundaries and numbering"""
    
    chapters = create_properly_numbered_chapters()
    
    # Read the input PDF
    with open(input_pdf_path, 'rb') as pdf_file:
        pdf_reader = pypdf.PdfReader(pdf_file)
        total_pages = len(pdf_reader.pages)
        print(f"Total pages in PDF: {total_pages}")
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Extract each chapter
        for chapter_name, start_page, end_page in chapters:
            # Adjust for 0-indexed pages
            start_idx = start_page - 1
            end_idx = min(end_page - 1, total_pages - 1)
            
            if start_idx >= total_pages:
                print(f"Skipping {chapter_name}: start page {start_page} exceeds total pages")
                continue
                
            # Create a new PDF for this chapter
            pdf_writer = pypdf.PdfWriter()
            
            # Add pages to the chapter PDF
            for page_idx in range(start_idx, end_idx + 1):
                if page_idx < total_pages:
                    pdf_writer.add_page(pdf_reader.pages[page_idx])
            
            # Save the chapter PDF
            output_path = os.path.join(output_dir, f"{chapter_name}.pdf")
            with open(output_path, 'wb') as output_file:
                pdf_writer.write(output_file)
            
            print(f"Created: {output_path} (pages {start_page}-{end_page})")

if __name__ == "__main__":
    input_pdf = "/home/user/multi_sensor_slam_ws/docs/SLAM_handbook.pdf"
    output_directory = "/home/user/multi_sensor_slam_ws/docs/chapters"
    
    # Remove old chapters directory
    if os.path.exists(output_directory):
        import shutil
        shutil.rmtree(output_directory)
    
    split_pdf_final(input_pdf, output_directory)
    print("Final corrected PDF splitting completed!")