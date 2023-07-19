# To run use
# $ streamlit run streamlit_demo_base.py

from yolor import *
import tempfile
import cv2

import streamlit as st

def main():

    def resize_video(video_path, width, height):
        """Redimensionar o vídeo para uma largura e altura específicas"""

        output_path = tempfile.mktemp(suffix='.mp4')
        vid = cv2.VideoCapture(video_path)
        codec = cv2.VideoWriter_fourcc(*'mp4v')
        fps = vid.get(cv2.CAP_PROP_FPS)
        video_writer = cv2.VideoWriter(output_path, codec, fps, (width, height))

        while True:
            ret, frame = vid.read()
            if not ret:
                break
            resized_frame = cv2.resize(frame, (width, height))
            video_writer.write(resized_frame)
        vid.release()
        video_writer.release()
        return output_path

    def add_logo(logo_path, width, height):
        """Read and return a resized logo"""
        logo = Image.open(logo_path)
        modified_logo = logo.resize((width, height))
        return modified_logo

    my_logo = add_logo(logo_path="vision.png", width=50, height=50)
    st.sidebar.image(my_logo)

    st.title("Object Tracking Dashboard YOLOR")

    st.sidebar.title("Settings")

    st.markdown(
        '''
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
        width="400px"
        }
        
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
        width="350px"
        margin-left="-400px"}
    </style>
    
    ''',
        unsafe_allow_html=True
    )

    st.sidebar.markdown("---")
    confidence = st.sidebar.slider("Confidence", min_value=0.0, max_value=1.0, value=0.25)
    width_video = st.sidebar.number_input("Width", min_value=300, max_value=2000, value=640)
    height_video = int(width_video*0.55)
    st.sidebar.markdown("---")

    save_img = st.sidebar.checkbox('Save Image')
    enable_GPU = st.sidebar.checkbox('GPU')

    night_demo = st.sidebar.checkbox('Demo Noturna')

    if night_demo:
        DEMO_VIDEO = 'video_demos/footage.mov'
    else:
        DEMO_VIDEO = 'video_demos/Traffic.mov'

    custom_classes = st.sidebar.checkbox("Use Custom Classes")
    assigned_classes_id = []
    if custom_classes:
        assigned_classes = st.sidebar.multiselect('Select The Custom Classes', list(names), default='car')
        for each in assigned_classes:
            assigned_classes_id.append(names.index(each))

    st.sidebar.markdown("---")
    video_file_buffer = st.sidebar.file_uploader("Upload video", type = ['mp4','mov','avi','asf','m4v'])


    tfflie = tempfile.NamedTemporaryFile(suffix='.mp4', delete=False)

    if not video_file_buffer:
        vid = cv2.VideoCapture(DEMO_VIDEO)
        tfflie.name = DEMO_VIDEO
        dem_vid = open(tfflie.name, 'rb')
        dem_bytes = dem_vid.read()

        st.sidebar.text('Input Video')
        st.sidebar.video(dem_bytes)
    else:
        tfflie.write(video_file_buffer.read())
        dem_vid = open(tfflie.name, 'rb')
        dem_bytes = dem_vid.read()

        st.sidebar.text('Input Video')
        st.sidebar.video(dem_bytes)

    print(tfflie.name)

    resized_video_path = resize_video(tfflie.name, width=width_video, height=height_video)  # Defina a largura e altura desejadas

    stframe = st.empty()
    st.sidebar.markdown("---")

    kpi1, kpi2, kpi3 = st.columns(3)

    with kpi1:
        st.markdown('**Fame Rate**')
        kpi1_text = st.markdown("0")

    with kpi2:
        st.markdown('**Tracked Objects**')
        kpi2_text = st.markdown("0")

    with kpi3:
        st.markdown('**Width**')
        kpi3_text = st.markdown("0")


    load_yolor_and_process_each_frame(resized_video_path, enable_GPU, confidence, assigned_classes_id,
                                      kpi1_text, kpi2_text, kpi3_text, stframe)

    st.text("Video Processed")
    vid.release()


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass