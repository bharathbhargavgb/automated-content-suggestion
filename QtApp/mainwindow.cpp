#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QProcess>
#include <QDebug>
#include <QFile>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);    
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_showSuggestion_clicked()
{
    QString text = "\"" + ui->content->toPlainText() + "\"";
    QProcess process;    
    process.start("python /Users/baaskab/hackathon/automated-content-suggestion/main.py " + text);
    process.waitForFinished(-1);
    QString output(process.readAllStandardOutput());
    qDebug() << output;

    QFile file("/Users/baaskab/hackathon/automated-content-suggestion/suggestion.txt");
    QString strings;
    if (file.open(QIODevice::ReadOnly | QIODevice::Text))
    {
        QTextStream in(&file);
        while (!in.atEnd()) {
            strings = in.readLine();
            ui->textBrowser->append(strings);
        }
    }
}

void MainWindow::on_pushButton_clicked()
{
    QProcess process;
    process.start("open /Users/baaskab/hackathon/automated-content-suggestion/images/");
    process.waitForFinished(-1);
}
