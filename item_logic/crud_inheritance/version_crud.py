from database import MONGOCRUD

class VersionCRUD(MONGOCRUD):

    def __init__(self):
        super().__init__('Version')

    async def get_versions_by_entryid(self, entry_id: str,reverted: bool):
        # Se obtienen las versiones en orden de novedad
        if(reverted):
            cursor = self.collection.find({"entry_id": entry_id , "reverted": False}).sort({"editDate" : -1})
        else:
            cursor = self.collection.find({"entry_id": entry_id}).sort({"editDate" : -1})

        versions = []

        async for document in cursor:
            # ddd
            # Convertir ObjectId a string y aplicar jsonable_encoder
            document['_id'] = str(document['_id'])  # Convertir ObjectId a string
            versions.append(document)

        return versions
    
    async def get_by_filter(self, filter):
        cursor = self.collection.find(filter).sort({"editDate" : -1})
        results = []
        async for document in cursor:
            document['_id'] = str(document['_id'])  # Convertir ObjectId a string
            results.append(document)
        
        return results