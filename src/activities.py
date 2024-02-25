import pprint


ACTIVITIES = [
    {
        "activityId": 10000001,
        "activityName": "Villanueva de la Ca\u00f1ada Running",
        "description": None,
        "startTimeLocal": "2023-11-06 07:17:39",
        "startTimeGMT": "2023-11-06 06:17:39",
        "activityType": {
            "typeId": 6,
            "typeKey": "trail_running",
            "parentTypeId": 1,
            "isHidden": False,
            "trimmable": True,
            "restricted": False
        },
        "eventType": {
            "typeId": 8,
            "typeKey": "fitness",
            "sortOrder": 3
        },
        "comments": None,
        "parentId": None,
        "distance": 5499.1298828125,
        "duration": 2016.001953125,
        "elapsedDuration": 2016.001953125,
        "movingDuration": 2013.177000939846,
        "elevationGain": 50.46319580078125,
        "elevationLoss": 56.019775390625,
        "averageSpeed": 2.7279999256134033,
        "maxSpeed": 3.246999979019165,
        "startLatitude": 40.43712920509279,
        "startLongitude": -3.994505926966667,
        "hasPolyline": True,
        "ownerId": 2360742,
        "ownerDisplayName": "osso73",
        "ownerFullName": "Oriol Pujol",
        "ownerProfileImageUrlSmall": "https://s3.amazonaws.com/garmin-connect-prod/profile_images/062b98cd-1711-423e-af61-1e35984b6e14-2360742.png",
        "ownerProfileImageUrlMedium": "https://s3.amazonaws.com/garmin-connect-prod/profile_images/b10a9d34-c298-461b-b5b2-0491c4c83702-2360742.png",
        "ownerProfileImageUrlLarge": "https://s3.amazonaws.com/garmin-connect-prod/profile_images/92512ce2-6918-4d62-9dff-a7605cbcd08e-2360742.png",
        "calories": 507.0,
        "bmrCalories": None,
        "averageHR": 158.0,
        "maxHR": 173.0,
        "averageRunningCadenceInStepsPerMinute": 151.234375,
        "maxRunningCadenceInStepsPerMinute": 161.0,
        "maxLapAvgRunCadence": None,
        "averageBikingCadenceInRevPerMinute": None,
        "maxBikingCadenceInRevPerMinute": None,
        "averageSwimCadenceInStrokesPerMinute": None,
        "maxSwimCadenceInStrokesPerMinute": None,
        "averageSwolf": None,
        "activeLengths": None,
        "steps": 5042,
        "conversationUuid": None,
        "conversationPk": None,
        "numberOfActivityLikes": None,
        "numberOfActivityComments": None,
        "likedByUser": None,
        "commentedByUser": None,
        "activityLikeDisplayNames": None,
        "activityLikeFullNames": None,
        "activityLikeProfileImageUrls": None,
        "requestorRelationship": None,
        "userRoles": [
            "SCOPE_GOLF_API_READ",
            "SCOPE_DIVE_API_WRITE",
            "SCOPE_CONNECT_WEB_TEMPLATE_RENDER",
            "SCOPE_DIVE_API_READ",
            "SCOPE_CONNECT_NON_SOCIAL_SHARED_READ",
            "SCOPE_DI_OAUTH_2_CLIENT_READ",
            "SCOPE_CONNECT_READ",
            "SCOPE_CONNECT_WRITE",
            "SCOPE_DI_OAUTH_2_TOKEN_ADMIN",
            "ROLE_CONNECTUSER",
            "ROLE_FITNESS_USER",
            "ROLE_WELLNESS_USER",
            "ROLE_CONNECT_2_USER"
        ],
        "privacy": {
            "typeId": 3,
            "typeKey": "subscribers"
        },
        "userPro": False,
        "courseId": None,
        "poolLength": None,
        "unitOfPoolLength": None,
        "hasVideo": False,
        "videoUrl": None,
        "timeZoneId": 124,
        "beginTimestamp": 1699251459000,
        "sportTypeId": 1,
        "avgPower": None,
        "maxPower": None,
        "aerobicTrainingEffect": 4.0,
        "anaerobicTrainingEffect": None,
        "strokes": None,
        "normPower": None,
        "leftBalance": None,
        "rightBalance": None,
        "avgLeftBalance": None,
        "max20MinPower": None,
        "avgVerticalOscillation": None,
        "avgGroundContactTime": None,
        "avgStrideLength": 107.87061703721857,
        "avgFractionalCadence": None,
        "maxFractionalCadence": None,
        "trainingStressScore": None,
        "intensityFactor": None,
        "vO2MaxValue": 42.0,
        "avgVerticalRatio": None,
        "avgGroundContactBalance": None,
        "lactateThresholdBpm": None,
        "lactateThresholdSpeed": None,
        "maxFtp": None,
        "avgStrokeDistance": None,
        "avgStrokeCadence": None,
        "maxStrokeCadence": None,
        "workoutId": None,
        "avgStrokes": None,
        "minStrokes": None,
        "deviceId": 3955295790,
        "minTemperature": None,
        "maxTemperature": None,
        "minElevation": 623.0,
        "maxElevation": 659.5493774414062,
        "avgDoubleCadence": None,
        "maxDoubleCadence": 161.0,
        "summarizedExerciseSets": None,
        "maxDepth": None,
        "avgDepth": None,
        "surfaceInterval": None,
        "startN2": None,
        "endN2": None,
        "startCns": None,
        "endCns": None,
        "summarizedDiveInfo": {
            "weight": None,
            "weightUnit": None,
            "visibility": None,
            "visibilityUnit": None,
            "surfaceCondition": None,
            "current": None,
            "waterType": None,
            "waterDensity": None,
            "summarizedDiveGases": [],
            "totalSurfaceTime": None
        },
        "activityLikeAuthors": None,
        "avgVerticalSpeed": None,
        "maxVerticalSpeed": 0.3937116350446429,
        "floorsClimbed": None,
        "floorsDescended": None,
        "manufacturer": "GARMIN",
        "diveNumber": None,
        "locationName": "Villanueva de la Ca\u00f1ada",
        "bottomTime": None,
        "lapCount": 9,
        "endLatitude": 40.43716935440898,
        "endLongitude": -3.994527719914913,
        "minAirSpeed": None,
        "maxAirSpeed": None,
        "avgAirSpeed": None,
        "avgWindYawAngle": None,
        "minCda": None,
        "maxCda": None,
        "avgCda": None,
        "avgWattsPerCda": None,
        "flow": None,
        "grit": None,
        "jumpCount": None,
        "caloriesEstimated": None,
        "caloriesConsumed": None,
        "waterEstimated": None,
        "waterConsumed": None,
        "maxAvgPower_1": None,
        "maxAvgPower_2": None,
        "maxAvgPower_5": None,
        "maxAvgPower_10": None,
        "maxAvgPower_20": None,
        "maxAvgPower_30": None,
        "maxAvgPower_60": None,
        "maxAvgPower_120": None,
        "maxAvgPower_300": None,
        "maxAvgPower_600": None,
        "maxAvgPower_1200": None,
        "maxAvgPower_1800": None,
        "maxAvgPower_3600": None,
        "maxAvgPower_7200": None,
        "maxAvgPower_18000": None,
        "excludeFromPowerCurveReports": None,
        "totalSets": None,
        "activeSets": None,
        "totalReps": None,
        "minRespirationRate": None,
        "maxRespirationRate": None,
        "avgRespirationRate": None,
        "trainingEffectLabel": None,
        "activityTrainingLoad": None,
        "avgFlow": None,
        "avgGrit": None,
        "minActivityLapDuration": 0.5120000243186951,
        "avgStress": None,
        "startStress": None,
        "endStress": None,
        "differenceStress": None,
        "maxStress": None,
        "aerobicTrainingEffectMessage": None,
        "anaerobicTrainingEffectMessage": None,
        "splitSummaries": [],
        "hasSplits": False,
        "maxBottomTime": None,
        "hasSeedFirstbeatProfile": None,
        "calendarEventId": None,
        "calendarEventUuid": None,
        "groupRideUUID": None,
        "avgGradeAdjustedSpeed": None,
        "avgWheelchairCadence": None,
        "maxWheelchairCadence": None,
        "avgJumpRopeCadence": None,
        "maxJumpRopeCadence": None,
        "gameName": None,
        "differenceBodyBattery": None,
        "gameType": None,
        "curatedCourseId": None,
        "matchedCuratedCourseId": None,
        "parent": False,
        "favorite": False,
        "decoDive": False,
        "pr": False,
        "purposeful": False,
        "manualActivity": False,
        "autoCalcCalories": False,
        "elevationCorrected": True,
        "atpActivity": False
    },
    {
        "activityId": 10000002,
        "activityName": "Bici el\u00edptica",
        "description": None,
        "startTimeLocal": "2023-08-05 10:11:01",
        "startTimeGMT": "2023-08-05 09:11:01",
        "activityType": {
            "typeId": 30,
            "typeKey": "elliptical",
            "parentTypeId": 29,
            "isHidden": False,
            "trimmable": True,
            "restricted": False
        },
        "eventType": {
            "typeId": 8,
            "typeKey": "fitness",
            "sortOrder": 3
        },
        "comments": None,
        "parentId": None,
        "distance": 6000.0,
        "duration": 3620.85009765625,
        "elapsedDuration": 3620.85009765625,
        "movingDuration": 0.0,
        "elevationGain": None,
        "elevationLoss": None,
        "averageSpeed": 1.6570694726376403,
        "maxSpeed": None,
        "startLatitude": None,
        "startLongitude": None,
        "hasPolyline": False,
        "ownerId": 2360742,
        "ownerDisplayName": "osso73",
        "ownerFullName": "Oriol Pujol",
        "ownerProfileImageUrlSmall": "https://s3.amazonaws.com/garmin-connect-prod/profile_images/062b98cd-1711-423e-af61-1e35984b6e14-2360742.png",
        "ownerProfileImageUrlMedium": "https://s3.amazonaws.com/garmin-connect-prod/profile_images/b10a9d34-c298-461b-b5b2-0491c4c83702-2360742.png",
        "ownerProfileImageUrlLarge": "https://s3.amazonaws.com/garmin-connect-prod/profile_images/92512ce2-6918-4d62-9dff-a7605cbcd08e-2360742.png",
        "calories": 644.0,
        "bmrCalories": None,
        "averageHR": 138.0,
        "maxHR": 154.0,
        "averageRunningCadenceInStepsPerMinute": 127.671875,
        "maxRunningCadenceInStepsPerMinute": 152.0,
        "maxLapAvgRunCadence": None,
        "averageBikingCadenceInRevPerMinute": None,
        "maxBikingCadenceInRevPerMinute": None,
        "averageSwimCadenceInStrokesPerMinute": None,
        "maxSwimCadenceInStrokesPerMinute": None,
        "averageSwolf": None,
        "activeLengths": None,
        "steps": 6546,
        "conversationUuid": None,
        "conversationPk": None,
        "numberOfActivityLikes": None,
        "numberOfActivityComments": None,
        "likedByUser": None,
        "commentedByUser": None,
        "activityLikeDisplayNames": None,
        "activityLikeFullNames": None,
        "activityLikeProfileImageUrls": None,
        "requestorRelationship": None,
        "userRoles": [
            "SCOPE_GOLF_API_READ",
            "SCOPE_DIVE_API_WRITE",
            "SCOPE_CONNECT_WEB_TEMPLATE_RENDER",
            "SCOPE_DIVE_API_READ",
            "SCOPE_CONNECT_NON_SOCIAL_SHARED_READ",
            "SCOPE_DI_OAUTH_2_CLIENT_READ",
            "SCOPE_CONNECT_READ",
            "SCOPE_CONNECT_WRITE",
            "SCOPE_DI_OAUTH_2_TOKEN_ADMIN",
            "ROLE_CONNECTUSER",
            "ROLE_FITNESS_USER",
            "ROLE_WELLNESS_USER",
            "ROLE_CONNECT_2_USER"
        ],
        "privacy": {
            "typeId": 3,
            "typeKey": "subscribers"
        },
        "userPro": False,
        "courseId": None,
        "poolLength": None,
        "unitOfPoolLength": None,
        "hasVideo": False,
        "videoUrl": None,
        "timeZoneId": 124,
        "beginTimestamp": 1699175461000,
        "sportTypeId": 0,
        "avgPower": None,
        "maxPower": None,
        "aerobicTrainingEffect": 2.5,
        "anaerobicTrainingEffect": None,
        "strokes": None,
        "normPower": None,
        "leftBalance": None,
        "rightBalance": None,
        "avgLeftBalance": None,
        "max20MinPower": None,
        "avgVerticalOscillation": None,
        "avgGroundContactTime": None,
        "avgStrideLength": 0.0,
        "avgFractionalCadence": None,
        "maxFractionalCadence": None,
        "trainingStressScore": None,
        "intensityFactor": None,
        "vO2MaxValue": None,
        "avgVerticalRatio": None,
        "avgGroundContactBalance": None,
        "lactateThresholdBpm": None,
        "lactateThresholdSpeed": None,
        "maxFtp": None,
        "avgStrokeDistance": None,
        "avgStrokeCadence": None,
        "maxStrokeCadence": None,
        "workoutId": None,
        "avgStrokes": None,
        "minStrokes": None,
        "deviceId": 3955295790,
        "minTemperature": None,
        "maxTemperature": None,
        "minElevation": None,
        "maxElevation": None,
        "avgDoubleCadence": None,
        "maxDoubleCadence": 152.0,
        "summarizedExerciseSets": None,
        "maxDepth": None,
        "avgDepth": None,
        "surfaceInterval": None,
        "startN2": None,
        "endN2": None,
        "startCns": None,
        "endCns": None,
        "summarizedDiveInfo": {
            "weight": None,
            "weightUnit": None,
            "visibility": None,
            "visibilityUnit": None,
            "surfaceCondition": None,
            "current": None,
            "waterType": None,
            "waterDensity": None,
            "summarizedDiveGases": [],
            "totalSurfaceTime": None
        },
        "activityLikeAuthors": None,
        "avgVerticalSpeed": None,
        "maxVerticalSpeed": None,
        "floorsClimbed": None,
        "floorsDescended": None,
        "manufacturer": "GARMIN",
        "diveNumber": None,
        "locationName": None,
        "bottomTime": None,
        "lapCount": 1,
        "endLatitude": None,
        "endLongitude": None,
        "minAirSpeed": None,
        "maxAirSpeed": None,
        "avgAirSpeed": None,
        "avgWindYawAngle": None,
        "minCda": None,
        "maxCda": None,
        "avgCda": None,
        "avgWattsPerCda": None,
        "flow": None,
        "grit": None,
        "jumpCount": None,
        "caloriesEstimated": None,
        "caloriesConsumed": None,
        "waterEstimated": None,
        "waterConsumed": None,
        "maxAvgPower_1": None,
        "maxAvgPower_2": None,
        "maxAvgPower_5": None,
        "maxAvgPower_10": None,
        "maxAvgPower_20": None,
        "maxAvgPower_30": None,
        "maxAvgPower_60": None,
        "maxAvgPower_120": None,
        "maxAvgPower_300": None,
        "maxAvgPower_600": None,
        "maxAvgPower_1200": None,
        "maxAvgPower_1800": None,
        "maxAvgPower_3600": None,
        "maxAvgPower_7200": None,
        "maxAvgPower_18000": None,
        "excludeFromPowerCurveReports": None,
        "totalSets": None,
        "activeSets": None,
        "totalReps": None,
        "minRespirationRate": None,
        "maxRespirationRate": None,
        "avgRespirationRate": None,
        "trainingEffectLabel": None,
        "activityTrainingLoad": None,
        "avgFlow": None,
        "avgGrit": None,
        "minActivityLapDuration": 3620.85009765625,
        "avgStress": None,
        "startStress": None,
        "endStress": None,
        "differenceStress": None,
        "maxStress": None,
        "aerobicTrainingEffectMessage": None,
        "anaerobicTrainingEffectMessage": None,
        "splitSummaries": [],
        "hasSplits": False,
        "maxBottomTime": None,
        "hasSeedFirstbeatProfile": None,
        "calendarEventId": None,
        "calendarEventUuid": None,
        "groupRideUUID": None,
        "avgGradeAdjustedSpeed": None,
        "avgWheelchairCadence": None,
        "maxWheelchairCadence": None,
        "avgJumpRopeCadence": None,
        "maxJumpRopeCadence": None,
        "gameName": None,
        "differenceBodyBattery": None,
        "gameType": None,
        "curatedCourseId": None,
        "matchedCuratedCourseId": None,
        "parent": False,
        "favorite": False,
        "decoDive": False,
        "pr": False,
        "purposeful": False,
        "manualActivity": False,
        "autoCalcCalories": False,
        "elevationCorrected": False,
        "atpActivity": False
    },
    {
        "activityId": 10000003,
        "activityName": "Bici el\u00edptica",
        "description": None,
        "startTimeLocal": "2022-11-04 11:41:00",
        "startTimeGMT": "2022-11-04 10:41:00",
        "activityType": {
            "typeId": 30,
            "typeKey": "elliptical",
            "parentTypeId": 29,
            "isHidden": False,
            "trimmable": True,
            "restricted": False
        },
        "eventType": {
            "typeId": 8,
            "typeKey": "fitness",
            "sortOrder": 3
        },
        "comments": None,
        "parentId": None,
        "distance": 5000.0,
        "duration": 3007.14501953125,
        "elapsedDuration": 3007.14501953125,
        "movingDuration": 0.0,
        "elevationGain": None,
        "elevationLoss": None,
        "averageSpeed": 1.6627066536532158,
        "maxSpeed": None,
        "startLatitude": None,
        "startLongitude": None,
        "hasPolyline": False,
        "ownerId": 2360742,
        "ownerDisplayName": "osso73",
        "ownerFullName": "Oriol Pujol",
        "ownerProfileImageUrlSmall": "https://s3.amazonaws.com/garmin-connect-prod/profile_images/062b98cd-1711-423e-af61-1e35984b6e14-2360742.png",
        "ownerProfileImageUrlMedium": "https://s3.amazonaws.com/garmin-connect-prod/profile_images/b10a9d34-c298-461b-b5b2-0491c4c83702-2360742.png",
        "ownerProfileImageUrlLarge": "https://s3.amazonaws.com/garmin-connect-prod/profile_images/92512ce2-6918-4d62-9dff-a7605cbcd08e-2360742.png",
        "calories": 507.0,
        "bmrCalories": 77.0,
        "averageHR": 135.0,
        "maxHR": 156.0,
        "averageRunningCadenceInStepsPerMinute": 129.46875,
        "maxRunningCadenceInStepsPerMinute": 161.0,
        "maxLapAvgRunCadence": None,
        "averageBikingCadenceInRevPerMinute": None,
        "maxBikingCadenceInRevPerMinute": None,
        "averageSwimCadenceInStrokesPerMinute": None,
        "maxSwimCadenceInStrokesPerMinute": None,
        "averageSwolf": None,
        "activeLengths": None,
        "steps": 5116,
        "conversationUuid": None,
        "conversationPk": None,
        "numberOfActivityLikes": None,
        "numberOfActivityComments": None,
        "likedByUser": None,
        "commentedByUser": None,
        "activityLikeDisplayNames": None,
        "activityLikeFullNames": None,
        "activityLikeProfileImageUrls": None,
        "requestorRelationship": None,
        "userRoles": [
            "SCOPE_GOLF_API_READ",
            "SCOPE_DIVE_API_WRITE",
            "SCOPE_CONNECT_WEB_TEMPLATE_RENDER",
            "SCOPE_DIVE_API_READ",
            "SCOPE_CONNECT_NON_SOCIAL_SHARED_READ",
            "SCOPE_DI_OAUTH_2_CLIENT_READ",
            "SCOPE_CONNECT_READ",
            "SCOPE_CONNECT_WRITE",
            "SCOPE_DI_OAUTH_2_TOKEN_ADMIN",
            "ROLE_CONNECTUSER",
            "ROLE_FITNESS_USER",
            "ROLE_WELLNESS_USER",
            "ROLE_CONNECT_2_USER"
        ],
        "privacy": {
            "typeId": 3,
            "typeKey": "subscribers"
        },
        "userPro": False,
        "courseId": None,
        "poolLength": None,
        "unitOfPoolLength": None,
        "hasVideo": False,
        "videoUrl": None,
        "timeZoneId": 124,
        "beginTimestamp": 1699094460000,
        "sportTypeId": 255,
        "avgPower": None,
        "maxPower": None,
        "aerobicTrainingEffect": 2.299999952316284,
        "anaerobicTrainingEffect": None,
        "strokes": None,
        "normPower": None,
        "leftBalance": None,
        "rightBalance": None,
        "avgLeftBalance": None,
        "max20MinPower": None,
        "avgVerticalOscillation": None,
        "avgGroundContactTime": None,
        "avgStrideLength": 0.0,
        "avgFractionalCadence": None,
        "maxFractionalCadence": None,
        "trainingStressScore": None,
        "intensityFactor": None,
        "vO2MaxValue": None,
        "avgVerticalRatio": None,
        "avgGroundContactBalance": None,
        "lactateThresholdBpm": None,
        "lactateThresholdSpeed": None,
        "maxFtp": None,
        "avgStrokeDistance": None,
        "avgStrokeCadence": None,
        "maxStrokeCadence": None,
        "workoutId": None,
        "avgStrokes": None,
        "minStrokes": None,
        "deviceId": 3955295790,
        "minTemperature": None,
        "maxTemperature": None,
        "minElevation": None,
        "maxElevation": None,
        "avgDoubleCadence": None,
        "maxDoubleCadence": 161.0,
        "summarizedExerciseSets": None,
        "maxDepth": None,
        "avgDepth": None,
        "surfaceInterval": None,
        "startN2": None,
        "endN2": None,
        "startCns": None,
        "endCns": None,
        "summarizedDiveInfo": {
            "weight": None,
            "weightUnit": None,
            "visibility": None,
            "visibilityUnit": None,
            "surfaceCondition": None,
            "current": None,
            "waterType": None,
            "waterDensity": None,
            "summarizedDiveGases": [],
            "totalSurfaceTime": None
        },
        "activityLikeAuthors": None,
        "avgVerticalSpeed": None,
        "maxVerticalSpeed": None,
        "floorsClimbed": None,
        "floorsDescended": None,
        "manufacturer": "GARMIN",
        "diveNumber": None,
        "locationName": None,
        "bottomTime": None,
        "lapCount": 1,
        "endLatitude": None,
        "endLongitude": None,
        "minAirSpeed": None,
        "maxAirSpeed": None,
        "avgAirSpeed": None,
        "avgWindYawAngle": None,
        "minCda": None,
        "maxCda": None,
        "avgCda": None,
        "avgWattsPerCda": None,
        "flow": None,
        "grit": None,
        "jumpCount": None,
        "caloriesEstimated": None,
        "caloriesConsumed": None,
        "waterEstimated": None,
        "waterConsumed": None,
        "maxAvgPower_1": None,
        "maxAvgPower_2": None,
        "maxAvgPower_5": None,
        "maxAvgPower_10": None,
        "maxAvgPower_20": None,
        "maxAvgPower_30": None,
        "maxAvgPower_60": None,
        "maxAvgPower_120": None,
        "maxAvgPower_300": None,
        "maxAvgPower_600": None,
        "maxAvgPower_1200": None,
        "maxAvgPower_1800": None,
        "maxAvgPower_3600": None,
        "maxAvgPower_7200": None,
        "maxAvgPower_18000": None,
        "excludeFromPowerCurveReports": None,
        "totalSets": None,
        "activeSets": None,
        "totalReps": None,
        "minRespirationRate": None,
        "maxRespirationRate": None,
        "avgRespirationRate": None,
        "trainingEffectLabel": None,
        "activityTrainingLoad": None,
        "avgFlow": None,
        "avgGrit": None,
        "minActivityLapDuration": 3007.14501953125,
        "avgStress": None,
        "startStress": None,
        "endStress": None,
        "differenceStress": None,
        "maxStress": None,
        "aerobicTrainingEffectMessage": None,
        "anaerobicTrainingEffectMessage": None,
        "splitSummaries": [],
        "hasSplits": False,
        "maxBottomTime": None,
        "hasSeedFirstbeatProfile": None,
        "calendarEventId": None,
        "calendarEventUuid": None,
        "groupRideUUID": None,
        "avgGradeAdjustedSpeed": None,
        "avgWheelchairCadence": None,
        "maxWheelchairCadence": None,
        "avgJumpRopeCadence": None,
        "maxJumpRopeCadence": None,
        "gameName": None,
        "differenceBodyBattery": None,
        "gameType": None,
        "curatedCourseId": None,
        "matchedCuratedCourseId": None,
        "parent": False,
        "favorite": False,
        "decoDive": False,
        "pr": False,
        "purposeful": False,
        "manualActivity": False,
        "autoCalcCalories": False,
        "elevationCorrected": False,
        "atpActivity": False
    },
    {
        "activityId": 10000004,
        "activityName": "Villanueva de la Ca\u00f1ada Running",
        "description": None,
        "startTimeLocal": "2021-11-03 07:28:38",
        "startTimeGMT": "2021-11-03 06:28:38",
        "activityType": {
            "typeId": 7,
            "typeKey": "street_running",
            "parentTypeId": 1,
            "isHidden": False,
            "trimmable": True,
            "restricted": False
        },
        "eventType": {
            "typeId": 8,
            "typeKey": "fitness",
            "sortOrder": 3
        },
        "comments": None,
        "parentId": None,
        "distance": 5388.33984375,
        "duration": 2086.583984375,
        "elapsedDuration": 2086.583984375,
        "movingDuration": 1998.0760192871094,
        "elevationGain": 30.66131591796875,
        "elevationLoss": 32.16961669921875,
        "averageSpeed": 2.5820000171661377,
        "maxSpeed": 3.0510001182556157,
        "startLatitude": 40.43714504688978,
        "startLongitude": -3.9945058431476355,
        "hasPolyline": True,
        "ownerId": 2360742,
        "ownerDisplayName": "osso73",
        "ownerFullName": "Oriol Pujol",
        "ownerProfileImageUrlSmall": "https://s3.amazonaws.com/garmin-connect-prod/profile_images/062b98cd-1711-423e-af61-1e35984b6e14-2360742.png",
        "ownerProfileImageUrlMedium": "https://s3.amazonaws.com/garmin-connect-prod/profile_images/b10a9d34-c298-461b-b5b2-0491c4c83702-2360742.png",
        "ownerProfileImageUrlLarge": "https://s3.amazonaws.com/garmin-connect-prod/profile_images/92512ce2-6918-4d62-9dff-a7605cbcd08e-2360742.png",
        "calories": 491.0,
        "bmrCalories": None,
        "averageHR": 151.0,
        "maxHR": 181.0,
        "averageRunningCadenceInStepsPerMinute": 150.28125,
        "maxRunningCadenceInStepsPerMinute": 163.0,
        "maxLapAvgRunCadence": None,
        "averageBikingCadenceInRevPerMinute": None,
        "maxBikingCadenceInRevPerMinute": None,
        "averageSwimCadenceInStrokesPerMinute": None,
        "maxSwimCadenceInStrokesPerMinute": None,
        "averageSwolf": None,
        "activeLengths": None,
        "steps": 4932,
        "conversationUuid": None,
        "conversationPk": None,
        "numberOfActivityLikes": None,
        "numberOfActivityComments": None,
        "likedByUser": None,
        "commentedByUser": None,
        "activityLikeDisplayNames": None,
        "activityLikeFullNames": None,
        "activityLikeProfileImageUrls": None,
        "requestorRelationship": None,
        "userRoles": [
            "SCOPE_GOLF_API_READ",
            "SCOPE_DIVE_API_WRITE",
            "SCOPE_CONNECT_WEB_TEMPLATE_RENDER",
            "SCOPE_DIVE_API_READ",
            "SCOPE_CONNECT_NON_SOCIAL_SHARED_READ",
            "SCOPE_DI_OAUTH_2_CLIENT_READ",
            "SCOPE_CONNECT_READ",
            "SCOPE_CONNECT_WRITE",
            "SCOPE_DI_OAUTH_2_TOKEN_ADMIN",
            "ROLE_CONNECTUSER",
            "ROLE_FITNESS_USER",
            "ROLE_WELLNESS_USER",
            "ROLE_CONNECT_2_USER"
        ],
        "privacy": {
            "typeId": 3,
            "typeKey": "subscribers"
        },
        "userPro": False,
        "courseId": None,
        "poolLength": None,
        "unitOfPoolLength": None,
        "hasVideo": False,
        "videoUrl": None,
        "timeZoneId": 124,
        "beginTimestamp": 1698992918000,
        "sportTypeId": 1,
        "avgPower": None,
        "maxPower": None,
        "aerobicTrainingEffect": 3.9000000953674316,
        "anaerobicTrainingEffect": None,
        "strokes": None,
        "normPower": None,
        "leftBalance": None,
        "rightBalance": None,
        "avgLeftBalance": None,
        "max20MinPower": None,
        "avgVerticalOscillation": None,
        "avgGroundContactTime": None,
        "avgStrideLength": 102.45229033535537,
        "avgFractionalCadence": None,
        "maxFractionalCadence": None,
        "trainingStressScore": None,
        "intensityFactor": None,
        "vO2MaxValue": 41.0,
        "avgVerticalRatio": None,
        "avgGroundContactBalance": None,
        "lactateThresholdBpm": None,
        "lactateThresholdSpeed": None,
        "maxFtp": None,
        "avgStrokeDistance": None,
        "avgStrokeCadence": None,
        "maxStrokeCadence": None,
        "workoutId": None,
        "avgStrokes": None,
        "minStrokes": None,
        "deviceId": 3955295790,
        "minTemperature": None,
        "maxTemperature": None,
        "minElevation": 637.5577392578125,
        "maxElevation": 659.7291870117188,
        "avgDoubleCadence": None,
        "maxDoubleCadence": 163.0,
        "summarizedExerciseSets": None,
        "maxDepth": None,
        "avgDepth": None,
        "surfaceInterval": None,
        "startN2": None,
        "endN2": None,
        "startCns": None,
        "endCns": None,
        "summarizedDiveInfo": {
            "weight": None,
            "weightUnit": None,
            "visibility": None,
            "visibilityUnit": None,
            "surfaceCondition": None,
            "current": None,
            "waterType": None,
            "waterDensity": None,
            "summarizedDiveGases": [],
            "totalSurfaceTime": None
        },
        "activityLikeAuthors": None,
        "avgVerticalSpeed": None,
        "maxVerticalSpeed": 0.375579833984375,
        "floorsClimbed": None,
        "floorsDescended": None,
        "manufacturer": "GARMIN",
        "diveNumber": None,
        "locationName": "Villanueva de la Ca\u00f1ada",
        "bottomTime": None,
        "lapCount": 7,
        "endLatitude": 40.43699149042368,
        "endLongitude": -3.9945376105606556,
        "minAirSpeed": None,
        "maxAirSpeed": None,
        "avgAirSpeed": None,
        "avgWindYawAngle": None,
        "minCda": None,
        "maxCda": None,
        "avgCda": None,
        "avgWattsPerCda": None,
        "flow": None,
        "grit": None,
        "jumpCount": None,
        "caloriesEstimated": None,
        "caloriesConsumed": None,
        "waterEstimated": None,
        "waterConsumed": None,
        "maxAvgPower_1": None,
        "maxAvgPower_2": None,
        "maxAvgPower_5": None,
        "maxAvgPower_10": None,
        "maxAvgPower_20": None,
        "maxAvgPower_30": None,
        "maxAvgPower_60": None,
        "maxAvgPower_120": None,
        "maxAvgPower_300": None,
        "maxAvgPower_600": None,
        "maxAvgPower_1200": None,
        "maxAvgPower_1800": None,
        "maxAvgPower_3600": None,
        "maxAvgPower_7200": None,
        "maxAvgPower_18000": None,
        "excludeFromPowerCurveReports": None,
        "totalSets": None,
        "activeSets": None,
        "totalReps": None,
        "minRespirationRate": None,
        "maxRespirationRate": None,
        "avgRespirationRate": None,
        "trainingEffectLabel": None,
        "activityTrainingLoad": None,
        "avgFlow": None,
        "avgGrit": None,
        "minActivityLapDuration": 128.5050048828125,
        "avgStress": None,
        "startStress": None,
        "endStress": None,
        "differenceStress": None,
        "maxStress": None,
        "aerobicTrainingEffectMessage": None,
        "anaerobicTrainingEffectMessage": None,
        "splitSummaries": [],
        "hasSplits": False,
        "maxBottomTime": None,
        "hasSeedFirstbeatProfile": None,
        "calendarEventId": None,
        "calendarEventUuid": None,
        "groupRideUUID": None,
        "avgGradeAdjustedSpeed": None,
        "avgWheelchairCadence": None,
        "maxWheelchairCadence": None,
        "avgJumpRopeCadence": None,
        "maxJumpRopeCadence": None,
        "gameName": None,
        "differenceBodyBattery": None,
        "gameType": None,
        "curatedCourseId": None,
        "matchedCuratedCourseId": None,
        "parent": False,
        "favorite": False,
        "decoDive": False,
        "pr": False,
        "purposeful": False,
        "manualActivity": False,
        "autoCalcCalories": False,
        "elevationCorrected": True,
        "atpActivity": False
    }
]

if __name__ == '__main__':
    pprint.pprint(ACTIVITIES)
    print(len(ACTIVITIES))