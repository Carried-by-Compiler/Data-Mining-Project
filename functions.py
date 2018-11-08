def num_missing_values(df):
    print(df.apply(lambda x: sum(x.isnull()), axis=0))

def fill_empty_values(df):
    headers = list(df)
    
    for heading in headers:
        
        if df[heading].dtype.name == "float64":
            df[heading].fillna(df[heading].mean(), inplace=True)
            
        elif df[heading].dtype.name == "object":
            
            # getting the key that has the largest value
            values = df[heading].value_counts()
            keys = list(values.keys())
            currentMax = 0
            currentMaxKey = ""
            for key in keys:
                if values[key] > currentMax:
                    currentMax = values[key]
                    currentMaxKey = key
            
            # set empty cells with the key with the max value
            df[heading].fillna(currentMaxKey, inplace=True)

def get_categorical_headings(df):
    
    headings = list(df)
    cat_headings = []
    for h in headings:
        if df[h].dtype.name != "float64":
            cat_headings.append(h)
    
    return cat_headings

def encode_categorical(df):
    
    cat_headings = get_categorical_headings(df)
    le = LabelEncoder()
    for heading in cat_headings:
        df[heading] = le.fit_transform(df[heading])
        
    df.dtypes

def classification_model(model, data, predictors, outcome):
    #Fit the model:
    model.fit(data[predictors],data[outcome])

    #Make predictions on training set:
    predictions = model.predict(data[predictors])

    #Print accuracy
    accuracy = metrics.accuracy_score(predictions,data[outcome])
    print ("Accuracy : %s" % "{0:.3%}".format(accuracy))

    #Perform k-fold cross-validation with 5 folds
    kf = KFold(5, True, 1)
    error = []
    for train, test in kf.split(data):
        # Filter training data
        train_predictors = (data[predictors].iloc[train,:])

        # The target we're using to train the algorithm.
        train_target = data[outcome].iloc[train]

        # Training the algorithm using the predictors and target.
        model.fit(train_predictors, train_target)

        #Record error from each cross-validation run
        error.append(model.score(data[predictors].iloc[test,:], data[outcome].iloc[test]))

    print ("Cross-Validation Score : %s" % "{0:.3%}".format(np.mean(error)))

    #Fit the model again so that it can be refered outside the function:
    model.fit(data[predictors],data[outcome]) 