FROM debian:bullseye

SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get install -y python3 \
    xvfb python3 \
    build-essential \
    libqt5core5a \
    libqt5gui5 \
    libxcb1 \
    libx11-xcb1 \
    libxcb-xtest0-dev \
    libxcb-xinerama0-dev \
    libxcb-shape0-dev \
    libxcb-xkb-dev \
    libxkbcommon-x11-dev \
    libx11-dev \
    python3-venv
RUN python3 -m venv /my_env && \
    bash -c "source /my_env/bin/activate && pip install --upgrade pip && pip install PyQt5 Pytest && echo $PATH"
ENV PATH="/my_env/bin:$PATH"
WORKDIR /progetto_software_avanzata
COPY requirements.txt requirements.txt
COPY . .
CMD ["/bin/bash", "-c", "Xvfb :1 -screen 0 1024x768x24 & export DISPLAY=:1 && python main.py"]