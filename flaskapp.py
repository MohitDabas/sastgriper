from flask import Flask,render_template,jsonify,request,json
import sastgrep
import os
import pickle
app=Flask(__name__)

FolderMark=''

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/demo')
def demo():
    return render_template('demo.html')

@app.route('/uf')
def uf():
    return render_template('uf.html')


@app.route('/folder_mark',methods=['GET','POST'])
def folder_mark():
    global FolderMark
    FolderMark=request.form['FolderMarked']
    FileObject=open("fm",'wb')
    pickle.dump(FolderMark,FileObject)
    FileObject.close()
    return jsonify(FolderMark)

@app.route('/get_regex',methods=['GET','POST'])
def get_regex():
    RegExp=request.form['Regexp']
    FileObject=open("fm",'rb')
    FolderMark=pickle.load(FileObject)
    print(FolderMark)
    Data=sastgrep.command_rec(RegExp,FolderMark)
    return jsonify(Data)

@app.route('/open_viscode',methods=['GET','POST'])
def open_viscode():
    PathNLineNum=request.form['PathNLineNum']
    os.system("code -g "+PathNLineNum)
    return jsonify(PathNLineNum)


if __name__=='__main__':
    app.run(debug=True)

