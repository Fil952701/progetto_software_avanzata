FROM debian:bullseye

SHELL ["/bin/bash", "-c"]

ENV QT_DEBUG_PLUGINS=1
ENV QT_QPA_PLATFORM='xcb'
ENV XDG_RUNTIME_DIR=/tmp
RUN echo "export QT_QPA_PLATFORM=xcb" >> ~/.bashrc
RUN apt-get update && apt-get install -y python3 \
        xvfb \
        xvfb python3-dev \
        xvfb python3 \
        build-essential \
        ca-certificates \
        libqt5core5a \
        libqt5gui5 \
        libxcb1 \
        qtbase5-private-dev \
        git \
        libx11-xcb1 \
        libxcb-xkb1 \
        libxcb-cursor0 \
        libxcb-icccm4 \
        libxcb-image0 \
        libxcb-keysyms1 \
        libxcb-render-util0 \
        libxcb-xfixes0 \
        libxcb-randr0 \
        libxcb-xtest0-dev \
        libxcb-xinerama0 \
        libxcb-xinerama0-dev \
        libxcb-shape0-dev \
        libxcb-xkb-dev \
        libxcb-util1 \
        libxkbcommon-x11-0 \
        libxkbcommon-x11-dev \
        libx11-dev \
        python3-venv

RUN python3 -m venv /my_env && \
    bash -c "source /my_env/bin/activate && pip install --upgrade pip && pip install PyQt5 Pytest python-dateutil faker && echo $PATH"
ENV PATH="/my_env/bin:$PATH"

WORKDIR /progetto_software_avanzata
COPY requirements.txt requirements.txt
COPY . .

RUN rm /my_env/lib/python3.9/site-packages/PyQt5/Qt5/plugins/imageformats/libqpdf.so

CMD ["/bin/bash", "-c", "Xvfb :1 -screen 0 1024x768x24 & sleep 5; export DISPLAY=:1; python3 main.py"]