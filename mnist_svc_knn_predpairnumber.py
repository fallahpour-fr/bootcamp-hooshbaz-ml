# Class that calculate accuracy and confusion matrix for model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

class pred_pair_num():
  def __init__(self,df,pair):
      self.df=df
      self.pair=pair
      
  def sepraite_df(self):
      class_1, class_2 = self.pair
      self.class_1=class_1
      self.class_2=class_2
      selected_df=self.df[self.df['target'].isin([class_1,class_2])]
      selected_X=selected_df.loc[:,selected_df.columns !='target']
      selected_y=selected_df['target'] 
      self.selected_X=selected_X
      self.selected_y=selected_y
      
  def train_model_return_acc(self):
      self.sepraite_df()
      X_train_pair, X_test_pair, y_train_pair, y_test_pair = train_test_split(self.selected_X, self.selected_y, test_size=0.33, random_state=42)
      svc_model=self.model
      svc_model.fit(X_train_pair,y_train_pair)
      y_pred_pair=svc_model.predict(X_test_pair)
      acc=accuracy_score(y_test_pair,y_pred_pair)
      cm=confusion_matrix(y_test_pair,y_pred_pair)  

      obj={}
      obj['model']=self.pair
      obj['accuracy']=acc
      obj[f'False detect {self.class_1}']=cm[0,1]
      obj[f'False detect {self.class_2}']=cm[1,0] 

      return obj