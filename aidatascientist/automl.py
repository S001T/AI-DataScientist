from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    accuracy_score,
    r2_score
)

from sklearn.ensemble import (
    RandomForestClassifier,
    RandomForestRegressor
)

from sklearn.tree import (
    DecisionTreeClassifier,
    DecisionTreeRegressor
)


class AutoMLTrainer:

    def __init__(
        self,
        df,
        target
    ):

        self.df = df
        self.target = target

    def prepare(self):

        X = self.df.drop(
            columns=[self.target]
        )

        X = X.select_dtypes(
            include="number"
        )

        y = self.df[self.target]

        return X, y

    def detect_task(
        self,
        y
    ):

        if y.nunique() <= 20:
            return "classification"

        return "regression"

    def train(self):

        X, y = self.prepare()

        task = self.detect_task(
            y
        )

        X_train, X_test, y_train, y_test = (
            train_test_split(
                X,
                y,
                test_size=0.2,
                random_state=42
            )
        )

        if task == "classification":

            models = {

                "RandomForest":
                RandomForestClassifier(
                    random_state=42
                ),

                "DecisionTree":
                DecisionTreeClassifier(
                    random_state=42
                )
            }

            best_score = 0
            best_model = None

            for name, model in models.items():

                model.fit(
                    X_train,
                    y_train
                )

                predictions = model.predict(
                    X_test
                )

                score = accuracy_score(
                    y_test,
                    predictions
                )

                if score > best_score:

                    best_score = score
                    best_model = name

            return {
                "task": task,
                "best_model": best_model,
                "score": float(best_score)
            }

        else:

            models = {

                "RandomForest":
                RandomForestRegressor(
                    random_state=42
                ),

                "DecisionTree":
                DecisionTreeRegressor(
                    random_state=42
                )
            }

            best_score = float("-inf")
            best_model = None

            for name, model in models.items():

                model.fit(
                    X_train,
                    y_train
                )

                predictions = model.predict(
                    X_test
                )

                try:

                    score = r2_score(
                        y_test,
                        predictions
                    )

                except:

                    score = -999999

                if score > best_score:

                    best_score = score
                    best_model = name

            return {
                "task": task,
                "best_model": best_model,
                "score": float(best_score)
            }