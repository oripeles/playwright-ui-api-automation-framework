FROM mcr.microsoft.com/playwright/python:v1.58.0-jammy


WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

RUN apt-get update && apt-get install -y default-jre wget && \
    ALLURE_VERSION="2.27.0" && \
    wget -qO /tmp/allure.tgz "https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}.tgz" && \
    tar -xzf /tmp/allure.tgz -C /opt/ && \
    ln -sf "/opt/allure-${ALLURE_VERSION}/bin/allure" /usr/local/bin/allure && \
    rm /tmp/allure.tgz

COPY . .

CMD ["pytest", "-n", "4", "--alluredir=allure-results"]
