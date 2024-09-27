FROM debian:bullseye

SHELL ["/bin/bash", "-c"]

ENV QT_DEBUG_PLUGINS=1
ENV QT_QPA_PLATFORM='xcb'
ENV XDG_RUNTIME_DIR=/tmp
ENV DISPLAY=:0

RUN apt-get update && apt-get install -y python3 \
        python3-dev \
        poppler-utils \
        qpdf \
        libpoppler-qt5-dev \
        procps \
        xauth \
        xvfb \
        build-essential \
        ca-certificates \
        libqt5core5a \
        libqt5gui5 \
        qtbase5-private-dev \
        git \
        libx11-xcb1 \
        libxcb1 \
        libxcb-util1 \
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
        libxkbcommon-x11-0 \
        libxkbcommon-x11-dev \
        libx11-dev \
        python3-venv \
        libwayland-dev \
        qtwayland5 \
        qtbase5-dev \
        libwayland-dev \
        libc6 \
        libqt5pdfwidgets5 \
        libwayland-egl1-mesa \
        libwayland-server0 \
        libwayland-egl1 \
        libwayland-cursor0 \
        libwayland-client0 \
        libqt5waylandclient5 \
        libqt5waylandcompositor5 \
        wayland-protocols \
        libgles2-mesa-dev \
        libxkbcommon-dev \
        weston


RUN python3 -m venv /my_env && \
    bash -c "source /my_env/bin/activate && pip install --upgrade PyQt5 pip && pip install PyQt5 Pytest python-dateutil faker && echo $PATH"

ENV PATH="/my_env/bin:$PATH"


WORKDIR /progetto_software_avanzata
COPY requirements.txt requirements.txt
COPY . .

RUN chmod 700 /tmp && rm /my_env/lib/python3.9/site-packages/PyQt5/Qt5/plugins/imageformats/libqpdf.so
#RUN export QT_QPA_PLATFORM_PLUGIN_PATH=/usr/lib/x86_64-linux-gnu/qt5/plugins
RUN find / -name libqxcb.so > /tmp/xcb_plugin_path && \
    PLUGIN_PATH=$(head -n 1 /tmp/xcb_plugin_path) && \
    echo $PLUGIN_PATH && \
    export QT_QPA_PLATFORM_PLUGIN_PATH=$PLUGIN_PATH

EXPOSE 80

CMD ["/bin/bash", "-c", "Xvfb :0 -screen 0 1024x768x24 & sleep 5; export DISPLAY=:0; python3 main.py"]
