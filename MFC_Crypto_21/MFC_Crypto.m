clear
%%%%%%% STEP I, Load Training Data
X_Train_Raw = readtable('TrainData.csv');

%Switch Data from table to Array for X_train
num_row = size(X_Train_Raw,1);
num_col = size(X_Train_Raw,2);
X_train = zeros(num_row, num_col - 2);%!!!!
j = 1;
for i = 2:(num_col-1)
    a = X_Train_Raw(:,i);
    A = table2array(a);
    X_train(:,j) = A;
    j = j + 1;
end

%Switch Data from table to Array for Y
a = X_Train_Raw(:,end);
Y_train = table2array(a); 

%%%%% STEP II: Load Testing Data

X_Test_Raw = readtable('TestData.csv');
%Switch Data from table to Array for X
num_row = size(X_Test_Raw,1);
num_col = size(X_Test_Raw,2);
X_test = zeros(num_row, num_col - 2);
j = 1;
for i = 2:(num_col-1)
    a = X_Test_Raw(:,i);
    A = table2array(a);
    X_test(:,j) = A;
    j = j + 1;
end
a = X_Test_Raw(:,end);
Y_test = table2array(a); 

%%%%%%STEP III: Load CV Data
X_CV_Raw = readtable('CVData.csv');
%Switch Data from table to Array for X
num_row = size(X_CV_Raw,1);
num_col = size(X_CV_Raw,2);
X_CV = zeros(num_row, num_col - 2);
j = 1;
for i = 2:(num_col-1)
    a = X_CV_Raw(:,i);
    A = table2array(a);
    X_CV(:,j) = A;
    j = j + 1;
end
a = X_CV_Raw(:,end);
Y_CV = table2array(a); 


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% FINISHED LOADING DATA%%%%%%%%%%%%%%%%%%%%%%


%%% Part 2 Cost Function

%X_train has 2100 examples, each row is an example. 
%There are 17 features in each example

%1) Unregularized cost function for logical regression
% J(theta) 
    
    
